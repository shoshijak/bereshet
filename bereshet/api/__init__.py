from flask import Blueprint

bp = Blueprint("api", __name__)

# from bereshet.models.makor import Makor
from bereshet.elements.mechaber import Mechaber

# from bereshet.models.sefer import Sefer
