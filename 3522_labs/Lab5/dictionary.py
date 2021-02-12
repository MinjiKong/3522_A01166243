import difflib
from file_handler import *


class Dictionary:
    """
    Dictionary class the emulates a dictionary object. You can load data from a file and query from it.
    """

    def __init__(self, file_extension):
        """
        Initializes a dictionary with a selected file extension and data set.
        :param file_extension: The type of file extension.
        """
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

    @property
    def data(self):
        """
        Gets the data in a Dictionary object.
        """
        return self._data


def main():
    """
    Main program for to run the functions.
    """
    dictionary = Dictionary('.json')
    dictionary.load_dictionary("data.json")

    val = None

    while val != "exitprogram":
        if dictionary.data:
            val = input("Input the word you are looking for here, or type 'exitprogram' to leave: ")
            if val != "exitprogram":
                word_list = dictionary.query_dictionary(val)
                print(word_list)
                for string in word_list:
                    FileHandler.write_lines("new.txt", val + ": " + string + "\n")

    print("Thanks for checking out the dictionary!")


if __name__ == "__main__":
    main()
