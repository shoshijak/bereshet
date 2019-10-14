"""
Defines API to Bereshet's functionalities.

APIs that do not rely on the web browser and make no assumptions about what kind of
client connects to them.

Defines the Blueprint that contains all API routes.
"""
from flask import Blueprint

bp = Blueprint("api", __name__)

from bereshet.api import errors

# from bereshet.models.makor import Makor
from bereshet.elements.mechaber import Mechaber

# from bereshet.models.sefer import Sefer

__all__ = ["errors", "Mechaber"]
