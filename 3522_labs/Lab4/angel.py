from user import User


class Angel(User):
    """
    This class represents an Angel user. An angel user has the highest threshold for a notification message and
    warning message.
    """

    def __init__(self, name, age, account_number, bank_name, bank_balance, budget_list):
        super().__init__(name, age, account_number, bank_name, bank_balance, budget_list)
        self._threshold = 90.0
        self._notification_message = "You've exceeded a budget category! Maybe cut back on the spending?"
