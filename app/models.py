from app import db, login_manager
from flask_login import UserMixin
from datetime import datetime


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password_hash = db.Column(db.String(128), nullable=False)
    name = db.Column(db.String(100), nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    # Relationships
    income = db.relationship('Income', backref='owner', lazy=True)

    def __repr__(self):
        return f'<User {self.email}>'


class Income(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    amount = db.Column(db.Float, nullable=False)
    client_name = db.Column(db.String(100), nullable=False)
    project_name = db.Column(db.String(150), nullable=False)
    date_received = db.Column(db.Date, nullable=False)
    status = db.Column(db.String(20), default='paid')  # paid, pending, overdue
    notes = db.Column(db.Text, nullable=True)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self):
        return f'<Income ${self.amount} from {self.client_name}>'
