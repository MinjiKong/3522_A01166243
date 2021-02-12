import json
import enum
import pathlib


class FileExtensions(enum.Enum):
    """
    Enum for file extensions.
    Can accept .txt and .json extensions.
    """
    TXT = '.txt'
    JSON = '.json'


class FileHandler:
    """
    File handler class that can load data from files or write lines to files.
    """

    def __init__(self):
        """
        Constructor for FileHandler. Initializes a file_data variable.
        """
        self._file_data = None

    @staticmethod
    def load_data(path, file_extension):
        """
        Loads the data from the file specified at the path.
        :param path: File path.
        :param file_extension: The type of extension.
        :precondition: The path and file extension must exist and be valid. If not, then the program will exit.
        :return: Returns the data in the file in a dictionary format. Dict.
        """
        if pathlib.Path(path).is_file():
            try:
                if file_extension == FileExtensions.TXT.value:
                    with open(path, mode="r", encoding="utf-8") as data_file:
                        data = data_file.read()
                        data_file.close()
                        return data
                elif file_extension == FileExtensions.JSON.value:
                    with open(path, mode="r", encoding="utf-8") as data_file:
                        data = json.load(data_file)
                        data_file.close()
                        return data
                else:
                    raise InvalidFileTypeError
            except InvalidFileTypeError as e:
                print(e)
        else:
            raise FileNotFoundError("File is not found!")

    @staticmethod
    def write_lines(path, lines):
        """
        Writes lines into a txt file (will create it if it does not exist).
        :param path: File path.
        :param lines: The lines to be written onto the text file.
        :precondition: The path must exist and be valid. If not, then the program will exit.
        :return: None
        """
        try:
            with open(path, "a") as data_file:
                data_file.write(lines)
                data_file.close()
        except Exception as e:
            print(e)


class InvalidFileTypeError(Exception):
    """
    Exception for invalid file type. Will be called if file type is not a TXT or JSON file.
    """

    def __init__(self):
        """
        Initializes the exception with a custom message.
        """
        super().__init__("File is not a TXT or JSON file!")
