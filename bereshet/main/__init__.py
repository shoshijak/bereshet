from flask import Blueprint

bp = Blueprint('main', __name__)

from bereshet.main import routes