import datetime

from flask_wtf import FlaskForm
from wtforms import StringField, FloatField, DateTimeField
from wtforms.validators import DataRequired


class ExpenseForm(FlaskForm):
    date = DateTimeField('Date', validators=[DataRequired()], default=datetime.datetime.today, format="%Y-%m-%d")
    name = StringField('Name', validators=[DataRequired()], default="Expense name")
    amount = FloatField('Amount', validators=[DataRequired()], default="0.00")

