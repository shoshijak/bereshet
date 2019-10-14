"""
Defines the functionalities related to elements of the Bereshet network.

Examples of elements include Mechabrim, Sefarim, Mekorot, ...
"""
from flask import Blueprint

bp = Blueprint("elements", __name__)

from bereshet.elements import routes

__all__ = ["bp", "routes"]
