from flask_wtf import FlaskForm
from wtforms.validators import DataRequired
from wtforms import StringField, SubmitField

class TaskForm(FlaskForm):
    description = StringField('Description', validators = [DataRequired()])
    submit = SubmitField('Add Task')