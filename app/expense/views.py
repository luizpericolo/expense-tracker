from flask import render_template, Blueprint, request, flash, redirect, url_for, session
from flask_login import login_required

from app.forms import ExpenseForm
from app.models import Expense
from app.utils import flash_form_errors

from app.repository import find_expense, insert_expense

expense = Blueprint('expense', __name__, template_folder='../static/templates')


@expense.route('/expense', methods=['GET'])
@login_required
def expense_get_add():
    return render_template('expense.html', form=ExpenseForm(), operation='Add', title='Add Expense')


@expense.route('/expense/<id_>', methods=['GET'])
@login_required
def expense_get_edit(id_):
    expense_ = find_expense(id_)
    form = ExpenseForm(obj=expense_)
    return render_template('expense.html', form=form, method='PUT', operation='Edit', title='Edit Expense')


@expense.route('/expense', methods=['POST'])
@login_required
def expense_post():
    form = ExpenseForm(request.form)
    if form.validate():
        new_expense = Expense(form.date.data, form.name.data, form.amount.data)
        success = insert_expense(new_expense, session.get('user_id'))
        if success:
            flash('Expense added successfully!', category='success')
        else:
            flash('Error adding expense', category='error')
    else:
        flash_form_errors(form)
    return redirect(url_for('.expense_get_add'))


@expense.route('/expense/<id>', methods=['PUT'])
@login_required
def expense_put():
    pass

