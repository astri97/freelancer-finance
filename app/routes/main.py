from flask import Blueprint, render_template, redirect, url_for, flash, request
from flask_login import login_required, current_user
from app import db
from app.models import Income
from datetime import datetime, date

main = Blueprint('main', __name__)


@main.route('/')
def index():
    if current_user.is_authenticated:
        return redirect(url_for('main.dashboard'))
    return redirect(url_for('auth.login'))


@main.route('/dashboard')
@login_required
def dashboard():
    income_entries = Income.query.filter_by(user_id=current_user.id)\
                                 .order_by(Income.date_received.desc()).all()

    total_income = sum(e.amount for e in income_entries if e.status == 'paid')
    pending_total = sum(e.amount for e in income_entries if e.status == 'pending')
    overdue_count = sum(1 for e in income_entries if e.status == 'overdue')

    return render_template('main/dashboard.html',
                           income_entries=income_entries,
                           total_income=total_income,
                           pending_total=pending_total,
                           overdue_count=overdue_count)


@main.route('/income/add', methods=['GET', 'POST'])
@login_required
def add_income():
    if request.method == 'POST':
        amount = request.form.get('amount')
        client_name = request.form.get('client_name')
        project_name = request.form.get('project_name')
        date_received = request.form.get('date_received')
        status = request.form.get('status', 'paid')
        notes = request.form.get('notes', '')

        if not amount or not client_name or not project_name or not date_received:
            flash('Please fill in all required fields.', 'error')
            return render_template('main/add_income.html')

        try:
            amount = float(amount)
            date_received = datetime.strptime(date_received, '%Y-%m-%d').date()
        except ValueError:
            flash('Invalid amount or date format.', 'error')
            return render_template('main/add_income.html')

        entry = Income(
            user_id=current_user.id,
            amount=amount,
            client_name=client_name,
            project_name=project_name,
            date_received=date_received,
            status=status,
            notes=notes
        )
        db.session.add(entry)
        db.session.commit()

        flash(f'Income of ${amount:,.2f} from {client_name} added!', 'success')
        return redirect(url_for('main.dashboard'))

    return render_template('main/add_income.html', today=date.today().isoformat())


@main.route('/income/delete/<int:income_id>', methods=['POST'])
@login_required
def delete_income(income_id):
    entry = Income.query.get_or_404(income_id)

    # Make sure users can only delete their own entries
    if entry.user_id != current_user.id:
        flash('Not authorized.', 'error')
        return redirect(url_for('main.dashboard'))

    db.session.delete(entry)
    db.session.commit()
    flash('Entry deleted.', 'info')
    return redirect(url_for('main.dashboard'))
