from user import User


class Troublemaker(User):
    """
    This class represents an Troublemaker user. An Troublemaker user has the second highest threshold for a notification
    message and warning message. They will also get locked out of transactions if they exceed a budget in category too
    much.
    """

    def __init__(self, name, age, account_number, bank_name, bank_balance, budget_list):
        super().__init__(name, age, account_number, bank_name, bank_balance, budget_list)
        self._threshold = 75.0
        self._notification_message = "You've exceeded a budget category! Maybe cut back on the spending?"
        self._lockout_threshold = 120.0
