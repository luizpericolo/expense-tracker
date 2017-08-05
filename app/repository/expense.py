from app import app
from app.models import Expense

from bson.objectid import ObjectId


def find_expense(expense_id):
    expense_data = app.config['EXPENSES_COLLECTION'].find_one({'_id': ObjectId(expense_id)})
    if expense_data:
        return Expense(**expense_data)
    return None


def find_user_expenses(user_id, limit=None):
    user_expenses = app.config['EXPENSES_COLLECTION'].find({'user_id': user_id})
    if limit:
        user_expenses = user_expenses.limit(limit)
    return map(lambda e: Expense(**e), user_expenses)


def insert_expense(expense):
    expense_data = _build_expense_data(expense)
    return app.config['EXPENSES_COLLECTION'].insert_one(expense_data)


def update_expense(expense_id, expense):
    expense_data = _build_expense_data(expense)
    return app.config['EXPENSES_COLLECTION'].find_one_and_replace(
        {'_id': ObjectId(expense_id)}, expense_data)


def delete_expense(expense_id):
    return app.config['EXPENSES_COLLECTION'].delete_one({'_id': ObjectId(expense_id)})


def _build_expense_data(expense):
    expense_data = {
        'name': expense.name,
        'date': expense.date,
        'amount': expense.amount,
        'user_id': expense.user_id,
    }

    if expense._id:
        expense_data['_id'] = expense._id

    return expense_data