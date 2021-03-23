from book import Book
from dvd import DVD
from scientific_journal import Journal
from item_factory_generator import ItemFactory


class LibraryItemGenerator(ItemFactory):
    """
    Generates a library item.
    """

    @staticmethod
    def create_book(user_dict):
        """
        Creates a book item based on the inputted parameters.

        :param user_dict: A tuple with these values in the following order:
        (Type of resource, call number, title of resource, number of copies, author/director/writer of the resource).
        :return: Book.
        """
        return Book(
            call_num=user_dict['call_number'],
            title=user_dict['title'],
            num_copies=user_dict['num_copies'],
            author=user_dict['author']
        )

    @staticmethod
    def create_scientific_journal(user_dict):
        """
        Creates a book item based on the inputted parameters.

        :param user_dict: A tuple with these values in the following order:
        (Type of resource, call number, title of resource, number of copies, author/director/writer of the resource).
        :return: Journal.
        """
        return Journal(
            call_num=user_dict['call_number'],
            title=user_dict['title'],
            num_copies=user_dict['num_copies'],
            names=user_dict['author'],
            issue_number=user_dict['issue_number'],
            publisher=user_dict['publisher']
        )

    @staticmethod
    def create_dvd(user_dict):
        """
        Creates a book item based on the inputted parameters.

        :param user_dict: A tuple with these values in the following order:
        (Type of resource, call number, title of resource, number of copies, author/director/writer of the resource).
        :return: DVD.
        """
        return DVD(
            call_num=user_dict['call_number'],
            title=user_dict['title'],
            num_copies=user_dict['num_copies'],
            director=user_dict['author'],
            release_date=user_dict['release_date'],
            region_code=user_dict['region_code']
        )

    def item_process(self, user_dict):
        library_item = user_dict['item_type']

        if library_item == 'Book':
            return self.create_book(user_dict)
        elif library_item == 'Journal':
            return self.create_scientific_journal(user_dict)
        elif library_item == 'DVD':
            return self.create_dvd(user_dict)
