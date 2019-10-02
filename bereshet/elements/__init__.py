from flask import Blueprint

bp = Blueprint('elements', __name__)

from bereshet.elements import routes