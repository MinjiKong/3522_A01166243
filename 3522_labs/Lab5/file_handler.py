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
                with open(path, mode="r", encoding="utf-8") as data_file:
                    data = json.load(data_file)
                    return data
            except Exception as e:
                print(e)
