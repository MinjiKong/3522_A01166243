from user import User
from datetime import datetime


class FAM:
    def __init__(self):
        self._user = User.load_test_user()
        self._transactions_list = []  # todo: move to budget class when implemented

    def record_transaction(self):
        """
        Record a transaction from user input.
        :return: String containing details about the transaction
        """
        print("Recording transaction...")
        transaction_timestamp = datetime.now()
        transaction_location = input("Enter the store or website you shopped at: ")
        transaction_amount = float(input("Enter the amount spent: "))

        # todo: refactor into Transaction object when implemented
        return f"Transaction at {transaction_location} on {transaction_timestamp}: ${transaction_amount} spent."

    def record_transaction_menu(self):
        """
        Handle user input for recording multiple transactions and displaying them.
        :return: None
        """
        print("Welcome to the Family Appointed Moderator (FAM)!")

        finished = False
        while not finished:
            selection = input("Type 't' to record a new transaction or anything else to quit: ")
            if selection.lower() == "t":
                self._transactions_list.append(self.record_transaction())
            else:
                finished = True

        print("All transactions:")
        for i in self._transactions_list:
            print(i)

        print("Thank you for using the FAM!")


def main():
    fam = FAM()
    fam.record_transaction_menu()


if __name__ == '__main__':
    main()