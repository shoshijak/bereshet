from flask import request
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, TextAreaField
from wtforms.validators import ValidationError, DataRequired, Length

# from bereshet.models.makor import Makor
from bereshet.elements.mechaber import Mechaber

# from bereshet.models.sefer import Sefer

#
