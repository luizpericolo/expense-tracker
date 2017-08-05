from app import app

from flask import render_template, Blueprint, request, flash, redirect, url_for
from flask_login import login_required

from app.forms import ExpenseForm
from app.models import Expense
from app.utils import flash_form_errors

expense = Blueprint('expense', __name__, template_folder='../static/templates')


@expense.route('/expense', methods=['GET'])
@login_required
def expense_get_add():
    return render_template('expense.html', form=ExpenseForm())


@expense.route('/expense/<id>', methods=['GET'])
@login_required
def expense_get_edit(id):
    expense = app.config['EXPENSES_COLLECTION'].find({'_id': id})
    form = ExpenseForm(expense)

    return render_template('expense.html', form=form, method='PUT')


@expense.route('/expense', methods=['POST'])
@login_required
def expense_post():
    import pudb
    pudb.set_trace()
    form = ExpenseForm(request.form)
    if form.validate():
        new_expense = Expense(form.date.data, form.name.data, form.amount.data)
        app.config['EXPENSES_COLLECTION'].insert(
            {'date': new_expense.date, 'name': new_expense.name, 'amount': new_expense.amount})
        flash('Expense added successfully!', category='success')
    else:
        flash_form_errors(form)
    return redirect(url_for('.expense_get_add'))


@expense.route('/expense/<id>', methods=['PUT'])
@login_required
def expense_put():
    pass

