from app import app
from app.models import Expense

from bson.objectid import ObjectId


def find_expense(expense_id):
    expense_data = app.config['EXPENSES_COLLECTION'].find_one({'_id': ObjectId(expense_id)})
    if expense_data:
        return Expense(**expense_data)
    return None


def find_user_expenses(user_id, limit=None):
    import pudb
    pudb.set_trace()
    user_expenses = app.config['EXPENSES_COLLECTION'].find({'user_id': user_id})
    if limit:
        user_expenses = user_expenses.limit(limit)
    return map(lambda e: Expense(**e), user_expenses)


def insert_expense(expense, user_id):
    expense_data = {
        'name': expense.name,
        'date': expense.date,
        'amount': expense.amount,
        'user_id': user_id
    }
    return app.config['EXPENSES_COLLECTION'].insert_one(expense_data)


def update_expense(expense):
    pass

def delete_expense(expense_id):
    pass