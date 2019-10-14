"""
Configures the Flask app, its database and other dependencies.

How ? What is needed?
"""

import os
from dotenv import load_dotenv

BASEDIR = os.path.abspath(os.path.dirname(__file__))
load_dotenv(os.path.join(BASEDIR, ".env"))


class Config:
    """
    Holds all configuration data and allows configuring based on a .env file.

    How? What is needed?
    """

    DEBUG = False
    TESTING = False
    SECRET_KEY = os.environ.get("SECRET_KEY") or "you-will-never-guess"
    SQLALCHEMY_DATABASE_URI = os.environ.get(
        "DATABASE_URL"
    ) or "sqlite:///" + os.path.join(BASEDIR, "bereshet.db")
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    LOG_TO_STDOUT = os.environ.get("LOG_TO_STDOUT")
    ELEMENTS_PER_PAGE = 25
    REDIS_URL = os.environ.get("REDIS_URL") or "redis://"

    def __repr__(self):
        """Return a debug representation of the Config instance."""
        return "Config:\n" + "".join(
            [f"{attribute}: {value}" for attribute, value in self.__dict__.items()]
        )

    def __str__(self):
        """Return a human-readable representation of the Config instance."""
        return (
            f"Config:\n"
            f"Debug mode: {self.DEBUG},\n"
            f"Testing mode: {self.TESTING},\n"
            f"Database at: {self.SQLALCHEMY_DATABASE_URI}"
        )
