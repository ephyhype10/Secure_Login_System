from app import app, db
from models import User   # <-- IMPORTANT: Import the model

with app.app_context():
    db.create_all()

print("✅ Database Created Successfully!")