from flask import render_template, Blueprint, request, flash, redirect, url_for, session
from flask_login import login_required

from app.forms import ExpenseForm
from app.models import Expense
from app.utils import flash_form_errors

from app.repository import find_expense, insert_expense, update_expense, delete_expense

expense = Blueprint('expense', __name__, template_folder='../static/templates')


@expense.route('/expense', methods=['GET'])
@login_required
def expense_get_add():
    return render_template('expense.html', form=ExpenseForm(), operation='Add', title='Add Expense', action='expense')


@expense.route('/expense/<id_>', methods=['GET'])
@login_required
def expense_get_edit(id_):
    expense_ = find_expense(id_)
    form = ExpenseForm(obj=expense_)
    return render_template('expense.html', form=form, method='PUT', operation='Edit', title='Edit Expense', action='edit-expense/{}'.format(expense_._id))


@expense.route('/expense', methods=['POST'])
@login_required
def expense_post():
    form = ExpenseForm(request.form)
    if form.validate():
        new_expense = Expense(form.date.data, form.name.data, form.amount.data, user_id=session.get('user_id'))
        success = insert_expense(new_expense)
        if success:
            flash('Expense added successfully!', category='success')
        else:
            flash('Error adding expense', category='danger')
    else:
        flash_form_errors(form)
    return redirect(url_for('.expense_get_add'))


@expense.route('/edit-expense/<id_>', methods=['POST'])
@login_required
def expense_put(id_):
    form = ExpenseForm(request.form)
    if form.validate():
        edited_expense = Expense(form.date.data, form.name.data, form.amount.data, user_id=session.get('user_id'))
        success = update_expense(id_, edited_expense)
        if success:
            flash('Expense updated successfully!', category='success')
        else:
            flash('Error updating expense', category='danger')
    else:
        flash_form_errors(form)
    return redirect(url_for('site.home'))


@expense.route('/confirm-delete-expense/<id_>', methods=['GET'])
def confirm_delete(id_):
    expense = find_expense(id_)
    return render_template('confirm_delete.html', expense=expense)


@expense.route('/delete-expense/<id_>', methods=['GET'])
@login_required
def delete(id_):
    result = delete_expense(id_)
    if result.deleted_count:
        flash('Expense deleted successfully!', category='success')
    else:
        flash('Error deleting expense', category='danger')
    return redirect(url_for('site.home'))
