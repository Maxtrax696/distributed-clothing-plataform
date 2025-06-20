from flask import Flask
from app.routes import login_bp
from app.db import db

def create_app():
    app = Flask(__name__)
    app.config.from_prefixed_env()
    db.init_app(app)
    app.register_blueprint(login_bp)
    return app
