from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import ValidationError, DataRequired, Length
from bereshet.elements.mechaber import Mechaber

# class CreateMechaberForm(CreateElementForm):
class CreateMechaberForm(FlaskForm):
    mechabername = StringField(
        "Mechaber' given name", validators=[DataRequired(), Length(min=3, max=64)]
    )
    submit = SubmitField("Create a new Mechaber")

    def validate_mechabername(self, mechabername):
        # Do not use a mechabername which already exists
        mechaber = Mechaber.query.filter_by(mechabername=mechabername.data).first()
        if mechaber is not None:
            raise ValidationError("This mechabername is already used")
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
