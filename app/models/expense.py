class Expense:
    def __init__(self, date, name, amount, _id=None, user_id=None):
        self._id = _id
        self.date = date
        self.name = name
        self.amount = amount
        self.user_id = user_id
