import os, logging, rq
from logging.handlers import SMTPHandler, RotatingFileHandler
from flask import Flask, request, current_app
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_bootstrap import Bootstrap
from config import Config
from redis import Redis

db = SQLAlchemy()
migrate = Migrate()
bootstrap = Bootstrap()


def create_reshet(config_class=Config):
    reshet = Flask(__name__)
    reshet.config.from_object(config_class)

    # Init modules
    db.init_app(reshet)
    migrate.init_app(reshet, db)
    bootstrap.init_app(reshet)

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
