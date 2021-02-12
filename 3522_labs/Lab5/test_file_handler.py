from unittest import TestCase

from Lab5.file_handler import FileHandler


class TestFileHandler(TestCase):
    def test_load_data_json(self):
        """
        Tests if the data loads correctly with a json file.
        """
        self.assertTrue(FileHandler.load_data("data.json", ".json"))

    def test_load_data_txt(self):
        """
        Tests if the data loads correctly with a txt file.
        """
        self.assertTrue(FileHandler.load_data("new.txt", ".txt"))

    def test_load_data_fail_filepath(self):
        """
        Tests if the data load fails if an incorrect filepath is used.
        """
        self.assertRaises(FileNotFoundError, FileHandler.load_data, "cool.json", ".json")

    def test_load_data_fail_file_extension(self):
        """
        Tests if the data load fails if an incorrect file extension is used.
        """
        self.assertFalse(FileHandler.load_data("data.json", ".csv"))

    def test_write_lines_txt(self):
        """
        Tests if file is written to correctly. (The best way to see if this works is to check if the new.txt file
        receives new values.)
        """
        self.assertIsNone(FileHandler.write_lines("new.txt", "Hi!\nHi! 2\n"))
