from book import Book
from dvd import DVD
from scientific_journal import Journal


class LibraryItemGenerator:
    """
    Generates a library item.
    """

    @staticmethod
    def create_library_item(user_input):
        """
        Creates a library item based on the inputted parameters.

        :param user_input: A tuple with these values in the following order:
        (Type of resource, call number, title of resource, number of copies, author/director/writer of the resource).
        :return: Depending on the type of resource, a Book, DVD or Journal object.
        """
        if user_input[0] == "BOOK":
            book = Book(user_input[1], user_input[2], user_input[3], user_input[4])
            return book
        elif user_input[0] == "DVD":
            release_date = input("Enter release date: ")
            region_code = input("Enter region code: ")
            dvd = DVD(user_input[1], user_input[2], user_input[3], director=user_input[4], release_date=release_date,
                      region_code=region_code)
            return dvd
        elif user_input[0] == "Scientific Journal":
            issue_number = input("Enter issue number: ")
            publisher = input("Enter publisher: ")
            scientific_journal = Journal(user_input[1], user_input[2], user_input[3],
                                         names=user_input[4], issue_number=issue_number, publisher=publisher)
            return scientific_journal
