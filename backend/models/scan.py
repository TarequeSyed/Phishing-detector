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

    def __init__(self, email_text, heuristic_score, url_score, llm_score,
                 final_score, urls_found, llm_analysis):
        self.email_text = email_text
        self.heuristic_score = heuristic_score
        self.url_score = url_score
        self.llm_score = llm_score
        self.final_score = final_score
        self.urls_found = urls_found
        self.llm_analysis = llm_analysis