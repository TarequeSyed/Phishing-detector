from flask import Flask
from routes.analyze import analyze_bp
from models.scan import Scan
from database import db

def create_app():
    app = Flask(__name__)

    app.config["SQLALCHEMY_DATABASE_URI"] = "postgresql://tareque:001668@localhost/phishing_db"
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

    db.init_app(app)

    from routes.analyze import analyze_bp
    app.register_blueprint(analyze_bp)

    return app
