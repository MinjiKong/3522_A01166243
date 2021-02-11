import difflib
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
        :return: None
        """

        try:
            self._data = FileHandler.load_data(filepath, self._file_extension)
        except Exception as e:
            print(e)
            exit(-1)

    def query_dictionary(self, word):
        """
        Queries the dictionary for a specific word. If the word is not found, nothing is returned
        :param word: The word that we are querying for.
        :precondition: Word must be a String.
        :return: String
        """

        key_list = self._data.keys()
        try:
            found_key = difflib.get_close_matches(word.lower(), key_list, n=3, cutoff=0.6)
            return self._data[found_key[0]]
        except AttributeError as e:
            print(e)
        except IndexError as e:
            print(e)


def main():
    dictionary = Dictionary('.json')
    dictionary.load_dictionary("data.json")
    print(dictionary.query_dictionary(input("Input the word you are looking for here: ")))


if __name__ == "__main__":
    main()
