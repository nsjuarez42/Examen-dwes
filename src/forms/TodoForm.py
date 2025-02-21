from flask_wtf import FlaskForm
from wtforms import StringField,TextAreaField,SubmitField
from wtforms.validators import DataRequired

class TodoForm(FlaskForm):
    
    title = StringField("Title",validators=[DataRequired()])

    description = TextAreaField("Description",validators=[DataRequired()])

    submit = SubmitField("Add todo")