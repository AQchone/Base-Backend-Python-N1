# app/__init__.py
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from config import Config

db = SQLAlchemy()
ma = Marshmallow()


def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    # Initialize extensions
    db.init_app(app)
    ma.init_app(app)

    # Import and register blueprints
    from .routes import product_bp

    app.register_blueprint(product_bp, url_prefix="/api")

    return app
