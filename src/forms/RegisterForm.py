from flask_wtf import FlaskForm
from wtforms import StringField,PasswordField,EmailField,SubmitField
from wtforms.validators import DataRequired

class RegisterForm(FlaskForm):
    
    name = StringField("Name",validators=[DataRequired()])

    email = EmailField("Email",validators=[DataRequired()])

    password = PasswordField("Password",validators=[DataRequired()])

    username = StringField("Username",validators=[DataRequired()])
    submit = SubmitField("Register")

