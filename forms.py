from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, SubmitField, BooleanField,DateField
from wtforms.validators import DataRequired, Length

class CreateForm(FlaskForm):
    id = IntegerField()
    Title = StringField('Title',validators=[DataRequired(), Length(min=2, max=20)])
    description = StringField('Description')
    dateofcompletion = DateField('Date To Complete',validators=[DataRequired()])
    submit = SubmitField('ADD')
#
class UpdateForm(FlaskForm):
    id = IntegerField('id')
    Title = StringField('Title', validators=[DataRequired(), Length(min=2, max=20)])
    description = StringField('Description')
    dateofcompletion = DateField('Date To Complete', validators=[DataRequired()])
    submit = SubmitField('Update')
