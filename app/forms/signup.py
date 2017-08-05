from flask_wtf import Form
from wtforms import StringField, PasswordField
from wtforms.validators import DataRequired

class SignupForm(Form):

    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    confirm_password = PasswordField('Confirm Password', validators=[DataRequired()])