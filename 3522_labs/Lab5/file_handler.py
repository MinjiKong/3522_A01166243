import json
import enum
import pathlib


class FileExtensions(enum.Enum):
    TXT = '.txt'
    JSON = '.json'


class FileHandler:

    def __init__(self):
        self._file_data = None

    @staticmethod
    def load_data(path, file_extension):
        if pathlib.Path(path).is_file():
            try:
                if file_extension == FileExtensions.TXT:
                    with open(path, mode="r", encoding="utf-8") as data_file:
                        data = data_file.read()
                        data_file.close()
                        return data
                elif file_extension == FileExtensions.JSON:
                    with open(path, mode="r", encoding="utf-8") as data_file:
                        data = json.load(data_file)
                        data_file.close()
                        return data
                else:
                    raise InvalidFileTypeError
            except InvalidFileTypeError as e:
                print(e)

    @staticmethod
    def write_lines(path, lines):
        try:
            with open(path, "a") as data_file:
                data_file.write(lines)
                data_file.close()
        except Exception as e:
            print(e)


class InvalidFileTypeError(Exception):
    def __init__(self):
        super().__init__("File is not a TXT or JSON file!")
