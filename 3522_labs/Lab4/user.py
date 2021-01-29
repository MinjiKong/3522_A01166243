import abc


class User(abc.ABC):
    """
    Abstract base class that represents all the necessary information that a user must have to function in the
    FAM system.
    """

    def __init__(self, name, age, account_number, bank_name, bank_balance, budget_list):
        self._name = name
        self._age = age
        self._account_number = account_number
        self._bank_name = bank_name
        self._bank_balance = bank_balance
        self._budget_list = budget_list

    @staticmethod
    def load_test_user():
        """
        Create a test User for.. test purposes
        :return: User
        """
        return User(
            "Janelle",
            500,
            1234567,
            "TD",
            2000.00,
            [
                "Games and Entertainment",
                "Clothing and Accessories",
                "Eating Out",
                "Miscellaneous"
            ]  # todo: replace strings with budget objects when implemented
        )
