from learning_resource import LearningResource


class DVD(LearningResource):
    """
    A learning resource that is a DVD, includes the unique attributes, director, release date and region code.
    """

    def __init__(self, call_num, title, num_copies, director, release_date, region_code):
        """
        :param call_num: a string
        :param title: a string
        :param num_copies: an int
        :param author: a string
        :precondition call_num: a unique identifier
        :precondition num_copies: a positive integer
        """
        self._call_num = call_num
        self._title = title
        self._num_copies = num_copies
        self._director = director
        self._release_date = release_date
        self._region_code = region_code

    def increment_number_of_copies(self):
        """
        Set's the number of copies of a DVD
        :param value: a positive integer
        """
        self._num_copies += 1

    def decrement_number_of_copies(self):
        """
        Set's the number of copies of a DVD
        :param value: a positive integer
        """
        self._num_copies -= 1

    def get_num_copies(self):
        """
        Returns the number of copies that are available for this
        specific DVD.
        :return: an int
        """
        return self._num_copies

    def check_availability(self):
        """
        Returns True if the DVD is available and False otherwise
        :return: A Boolean
        """
        if self._num_copies > 0:
            return True
        else:
            return False

    def get_title(self):
        """
        Returns the title of the DVD
        :return: a string
        """
        return self._title

    @property
    def call_number(self):
        """
        Gets the call number for this DVD.
        :return: the call number.
        """
        return self._call_num

    def __str__(self):
        return f"---- DVD: {self.get_title()} ----\n" \
               f"Call Number: {self.call_number}\n" \
               f"Number of Copies: {self._num_copies}\n" \
               f"Director: {self._director}\n" \
               f"Release: {self._release_date}\n" \
               f"Region Code: {self._region_code}"
