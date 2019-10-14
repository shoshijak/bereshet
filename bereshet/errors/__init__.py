"""Defines all error functionalities."""
from flask import Blueprint

bp = Blueprint("errors", __name__)

from bereshet.errors import handlers

__all__ = ["handlers"]
