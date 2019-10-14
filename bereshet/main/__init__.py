"""Defines the main Bereshet functionalities."""
from flask import Blueprint

bp = Blueprint("main", __name__)

from bereshet.main import routes

__all__ = ["routes"]
