from app import create_app
from database import db

from models.scan import Scan

app = create_app()

with app.app_context():
    print("Creating database tables!!!")
    db.create_all()
    print("Tables created successfully!!!")