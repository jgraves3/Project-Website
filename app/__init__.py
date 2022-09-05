from flask import Flask, current_app
from config import Config
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

bootstrap = Bootstrap()
db = SQLAlchemy()
migrate = Migrate()

from app.ask import bp as ask_bp
from app.errors import bp as errors_bp

def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(config_class)
    app.register_blueprint(errors_bp)
    app.register_blueprint(ask_bp)

    db.init_app(app)
    migrate.init_app(app)
    bootstrap.init_app(app)
    return app
