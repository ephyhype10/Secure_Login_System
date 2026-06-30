# Secure Login System
 
A simple and secure user authentication system built with **Flask**, **Flask-Login**, **Flask-Bcrypt**, and **Flask-SQLAlchemy**. It provides user registration, login, logout, and protected dashboard/profile pages, with passwords hashed using bcrypt and strong password validation enforced on registration.
 
## Features
 
- User registration with email and username
- Strong password policy validation (minimum 8 characters, uppercase, lowercase, number, and special character)
- Secure password hashing using Flask-Bcrypt
- Login/logout session management with Flask-Login
- Protected routes (`/dashboard`, `/profile`) accessible only to authenticated users
- Flash messages for success/error feedback
- MySQL database integration via SQLAlchemy and PyMySQL
## Tech Stack
 
- **Backend:** Python, Flask
- **Database:** MySQL (via Flask-SQLAlchemy + PyMySQL)
- **Auth & Security:** Flask-Login, Flask-Bcrypt
- **Forms & Validation:** Flask-WTF, WTForms
- **Frontend:** Jinja2 templates, HTML/CSS
## Project Structure
 
```
Secure_Login_System/
├── app.py              # Flask app initialization (db, bcrypt, login manager)
├── config.py           # App configuration (secret key, database URI)
├── create_db.py        # Script to create database tables
├── models.py           # User model (SQLAlchemy)
├── forms.py            # Registration & login forms with validators
├── routes.py           # Application routes (home, register, login, dashboard, profile, logout)
├── requirements.txt    # Python dependencies
├── static/
│   └── css/
│       └── style.css
└── templates/
    ├── base.html
    ├── index.html
    ├── register.html
    ├── login.html
    ├── dashboard.html
    └── profile.html
```
 
## Getting Started
 
### Prerequisites
 
- Python 3.10+
- MySQL Server installed and running
### 1. Clone the repository
 
```bash
git clone <your-repo-url>
cd Secure_Login_System
```
 
### 2. Create and activate a virtual environment
 
```bash
python -m venv venv
 
# Windows
venv\Scripts\activate
 
# macOS/Linux
source venv/bin/activate
```
 
### 3. Install dependencies
 
```bash
pip install -r requirements.txt
```
 
### 4. Configure the database
 
Create a MySQL database (e.g. `secure_login`), then update `config.py` with your own database credentials and a strong secret key:
 
```python
class Config:
    SECRET_KEY = "your-own-random-secret-key"
    SQLALCHEMY_DATABASE_URI = "mysql+pymysql://<username>:<password>@localhost/secure_login"
    SQLALCHEMY_TRACK_MODIFICATIONS = False
```
 
> **Note:** It's recommended to load these values from environment variables instead of hardcoding them, especially before pushing to a public repository.
 
### 5. Create the database tables
 
```bash
python create_db.py
```
 
### 6. Run the application
 
```bash
python app.py
```
 
The app will be available at `http://127.0.0.1:5000/`.
 
## Usage
 
1. Visit the home page and register a new account.
2. Enter a password that satisfies the strength requirements (8+ characters, uppercase, lowercase, number, special character).
3. Log in with your registered email and password.
4. Access your protected dashboard and profile pages.
5. Log out when done.
## Security Notes
 
- Passwords are never stored in plain text — they are hashed using bcrypt before being saved to the database.
- Sensitive routes are protected using Flask-Login's `@login_required` decorator.
- Before deploying or committing to a public repository, replace the default `SECRET_KEY` and database credentials in `config.py` with environment variables, and add a `.env` / `config.py` entry to `.gitignore` if it contains real secrets.
## License
 
This project is open source and available for personal or educational use.
