# 💰 FreelancerFinance

A budget tracking web app built specifically for freelancers. Track income by client, monitor outstanding payments, and get a clear picture of your finances — without the complexity of full accounting software.

**Built with Python, Flask, and SQLAlchemy.**

---

## 🖥️ Live Demo

> Coming soon — deploying to Render.com

---

## ✨ Features

- **User Authentication** — secure registration and login with hashed passwords
- **Income Tracking** — log payments by client, project, amount, and date
- **Status Management** — mark income as Paid, Pending, or Overdue
- **Dashboard** — see total earned, pending payments, and overdue invoices at a glance
- **Responsive UI** — clean, minimal interface that works on desktop and mobile

---

## 🛠️ Tech Stack

| Layer | Technology |
|-------|-----------|
| Backend | Python 3, Flask |
| Database | SQLite (dev) → PostgreSQL (prod) |
| ORM | Flask-SQLAlchemy |
| Auth | Flask-Login, Flask-Bcrypt |
| Frontend | Jinja2 Templates, CSS |
| Deployment | Render.com *(coming soon)* |

---

## 🚀 Running Locally

**1. Clone the repo**
```bash
git clone https://github.com/astri97/freelancer-finance.git
cd freelancer-finance
```

**2. Create and activate a virtual environment**
```bash
python3 -m venv venv
source venv/bin/activate
```

**3. Install dependencies**
```bash
pip install -r requirements.txt
```

**4. Set up environment variables**
```bash
cp env.example .env
```

**5. Run the app**
```bash
python run.py
```

Open **http://127.0.0.1:5000** in your browser.

---

## 📁 Project Structure

```
freelancer-finance/
├── run.py                  # App entry point
├── requirements.txt        # Python dependencies
├── env.example             # Environment variable template
└── app/
    ├── __init__.py         # App factory & extensions
    ├── models.py           # Database models (User, Income)
    ├── routes/
    │   ├── auth.py         # Register, login, logout
    │   └── main.py         # Dashboard, income CRUD
    ├── templates/
    │   ├── base.html       # Shared layout
    │   ├── auth/           # Login & register pages
    │   └── main/           # Dashboard & income forms
    └── static/css/
        └── style.css       # App styles
```

---

## 🗺️ Roadmap

- [x] User authentication (register, login, logout)
- [x] Income tracking with client and project fields
- [x] Dashboard with financial summary
- [ ] Expense tracking with categories
- [ ] Client manager with per-client income breakdown
- [ ] CSV export
- [ ] Quarterly tax estimator
- [ ] Invoice PDF generator
- [ ] Stripe subscription (Free + Pro tiers)
- [ ] Deploy to Render.com

---

## 👩‍💻 About

Built by **Astri Hernandez Lanza** as a portfolio project to demonstrate full-stack Python development skills including Flask, SQLAlchemy, authentication, and database design.

- GitHub: [@astri97](https://github.com/astri97)

---

## 📄 License

MIT License — feel free to use this project as a reference.
