from flask import Flask
from app.routes import login_bp
from app.db import db
import os

def create_app():
    app = Flask(__name__)

    app.config["SQLALCHEMY_DATABASE_URI"] = os.getenv(
        "DATABASE_URL",
        "sqlite:///:memory:"  # fallback para pruebas si no hay PostgreSQL
    )

    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

    db.init_app(app)
    app.register_blueprint(login_bp)

    return app
