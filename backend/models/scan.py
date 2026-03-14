from database import db
from datetime import datetime

class Scan(db.Model):

    __tablename__ = "scans"

    id = db.Column(db.Integer, primary_key=True)

    email_text = db.Column(db.Text)

    heuristic_score = db.Column(db.Integer)
    url_score = db.Column(db.Integer)
    llm_score = db.Column(db.Integer)

    final_score = db.Column(db.Integer)

    urls_found = db.Column(db.Text)

    llm_analysis = db.Column(db.Text)

    created_at = db.Column(db.DateTime, default=datetime.utcnow)