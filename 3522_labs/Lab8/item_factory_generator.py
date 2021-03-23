import abc


class ItemFactory(abc.ABC):

    @staticmethod
    def create_book(user_dict):
        pass

    @staticmethod
    def create_scientific_journal(user_dict):
        pass

    @staticmethod
    def create_dvd(user_dict):
        pass

    def item_process(self, user_dict):
        """
        Accept a dict and determines which item to create based on type
        :param user_dict: dict representing item
        """
        pass
