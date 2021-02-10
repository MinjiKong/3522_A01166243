import json
from file_handler import *

class Dictionary:

    def __init__(self, file_extension):
        self._data = None
        self._file_extension = file_extension

    def load_dictionary(self, filepath):
        """
        Loads data into a dictionary.
        :param filepath: The file path to load the data into.
        :precondition: Filepath must be a string and a filepath to an actual file
        :return:
        """

        FileHandler.load_data(filepath, self._file_extension)
        return
