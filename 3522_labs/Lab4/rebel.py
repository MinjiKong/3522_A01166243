from user import User


class Rebel(User):
    """
    This class represents an Revel user. An Revel user has the lowest threshold for a notification
    message and warning message. They will also get locked out of transactions and their account if they exceed
    too many budgets in category.
    """

    def __init__(self, name, age, account_number, bank_name, bank_balance, budget_list):
        super().__init__(name, age, account_number, bank_name, bank_balance, budget_list)
        self._threshold = 50.0
        self._notification_message = "Hey! What are you doing, you've gone 50% on your budget! Stop spending mate!"
        self._lockout_threshold = 100.0
