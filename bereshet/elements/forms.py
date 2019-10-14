"""Defines Bereshet's forms."""
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import ValidationError, DataRequired, Length
from bereshet.elements.mechaber import Mechaber


# class CreateMechaberForm(CreateElementForm):
class CreateMechaberForm(FlaskForm):
    """
    Class CreateMechaberForm: f a form allowing to create a new 'Mechaber'.

    Members:
    x
    """

    mechaber_name = StringField(
        "Mechaber' given name", validators=[DataRequired(), Length(min=3, max=64)]
    )
    submit = SubmitField("Create a new Mechaber")

    def validate_mechaber_name(self, mechaber_name):
        """Validate the name of a Mechaber before accpeting it into the Database."""
        # Do not use a mechaber_name which already exists
        mechaber = Mechaber.query.filter_by(mechaber_name=mechaber_name.data).first()
        if mechaber is not None:
            raise ValidationError("This mechaber_name is already used")
        # TODO add more validation conditions
        # do not use a name that is among someone else is names
        # do not use a name which contains certain special characters
        # Start with a Capital letter

    # def validate_otherfields(self, fieldname):


# class CreateElementForm(FlaskForm):
#    post = TextAreaField('Say something', validators=[DataRequired()])
#    submit = SubmitField('Submit')

# class CreateMakorForm(CreateElementForm):
#    pass
#
# class EditElementForm(FlaskForm):
#    pass

# class SearchElementForm(FlaskForm):
#    q = StringField('Search', validators=[DataRequired()])
#
#    def __init__(self, *args, **kwargs):
#        if 'formdata' not in kwargs:
#            kwargs['formdata'] = request.args
#        if 'csrf_enabled' not in kwargs:
#            kwargs['csrf_enabled'] = False
#        super(SearchForm, self).__init__(*args, **kwargs)
