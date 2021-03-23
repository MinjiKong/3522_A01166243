from learning_resource import LearningResource


class Journal(LearningResource):
    """
    A learning resource that represents a DVD, includes the unique attributes, name, issue number and publisher.
    """

    def __init__(self, call_num, title, num_copies, names, issue_number, publisher):
        """
        :param call_num: a string
        :param title: a string
        :param num_copies: an int
        :param names: a string
        :precondition call_num: a unique identifier
        :precondition num_copies: a positive integer
        """
        self._call_num = call_num
        self._title = title
        self._num_copies = num_copies
        self._names = names
        self._issue_number = issue_number
        self._publisher = publisher

    @property
    def title(self):
        """
        Returns the title of the scientific journal
        :return: a string
        """
        return self._title

    def increment_number_of_copies(self):
        """
        Set's the number of copies of a scientific journal
        :param value: a positive integer
        """
        self._num_copies += 1

    def decrement_number_of_copies(self):
        """
        Set's the number of copies of a scientific journal
        :param value: a positive integer
        """
        self._num_copies -= 1

    @property
    def num_copies(self):
        """
        Returns the number of copies that are available for this
        specific scientific journal.
        :return: an int
        """
        return self._num_copies

    def check_availability(self):
        """
        Returns True if the scientific journal is available and False otherwise
        :return: A Boolean
        """
        if self._num_copies > 0:
            return True
        else:
            return False

    @property
    def call_number(self):
        """
        Gets the call number for this scientific journal.
        :return: the call number.
        """
        return self._call_num

    def __str__(self):
        return f"---- Scientific Journal: {self.title} ----\n" \
               f"Call Number: {self.call_number}\n" \
               f"Number of Copies: {self._num_copies}\n" \
               f"Names: {self._names}\n" \
               f"Issue Number: {self._issue_number}\n" \
               f"Publisher: {self._publisher}" \
