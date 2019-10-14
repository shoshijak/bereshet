"""Bereshet Application initialization and factory function."""

import os
import logging
from logging.handlers import RotatingFileHandler
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_bootstrap import Bootstrap
from config import Config

DB = SQLAlchemy()
MIGRATE = Migrate()
BOOTSTRAP = Bootstrap()


def create_reshet(config_class=Config):
    """Bereshet application factory."""
    reshet = Flask(__name__)
    reshet.config.from_object(config_class)

    # Init modules
    DB.init_app(reshet)
    MIGRATE.init_app(reshet, DB)
    BOOTSTRAP.init_app(reshet)

    # Register blueprints
    from bereshet.errors import bp as errors_bp

    reshet.register_blueprint(errors_bp)

    from bereshet.main import bp as main_bp

    reshet.register_blueprint(main_bp)

    from bereshet.api import bp as api_bp

    reshet.register_blueprint(api_bp, url_prefix="/api")

    # Error logging: only when not running in debug mode
    if not reshet.debug and not reshet.testing:
        if reshet.config["LOG_TO_STDOUT"]:
            stream_handler = logging.StreamHandler()
            stream_handler.setLevel(logging.INFO)
            reshet.logger.addHandler(stream_handler)
        else:
            if not os.path.exists("logs"):
                os.mkdir("logs")
            file_handler = RotatingFileHandler(
                "logs/microblog.log", maxBytes=10240, backupCount=10
            )
            file_handler.setFormatter(
                logging.Formatter(
                    "%(asctime)s %(levelname)s: %(message)s "
                    "[in %(pathname)s:%(lineno)d]"
                )
            )
            file_handler.setLevel(logging.INFO)
            reshet.logger.addHandler(file_handler)

        reshet.logger.setLevel(logging.INFO)
        reshet.logger.info("Reshet startup")

    return reshet


from bereshet import elements

__all__ = ["create_reshet", "elements"]
