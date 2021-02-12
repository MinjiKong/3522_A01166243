from unittest import TestCase

from Lab5.dictionary import Dictionary


class TestDictionary(TestCase):

    def test_load_dictionary_json(self):
        """
        Tests if the data loads correctly with a json file.
        """
        dictionary = Dictionary(".json")
        dictionary.load_dictionary("data.json")
        self.assertTrue(dictionary._data)

    def test_load_dictionary_txt(self):
        """
        Tests if the data loads correctly with a txt file.
        """
        dictionary = Dictionary(".txt")
        dictionary.load_dictionary("new.txt")
        self.assertTrue(dictionary._data)

    def test_load_dictionary_fail_filepath(self):
        """
        Tests if the data load fails with an incorrect filepath.
        """
        dictionary = Dictionary(".json")
        dictionary.load_dictionary("something.txt")
        self.assertFalse(dictionary._data)

    def test_load_dictionary_fail_file_extension(self):
        """
        Tests if the data load fails with an incorrect file extension.
        """
        dictionary = Dictionary(".csv")
        dictionary.load_dictionary("data.json")
        self.assertFalse(dictionary._data)

    def test_query_dictionary_correct_spelling(self):
        """
        Tests if the query works with an exact spelling.
        """
        dictionary = Dictionary(".json")
        dictionary.load_dictionary("data.json")
        self.assertEqual(dictionary.query_dictionary("aerodynamic"), ['Of or relating to aerodynamics.'])

    def test_query_dictionary_incorrect_spelling(self):
        """
        Tests if the query works with spelling that has errors.
        """
        dictionary = Dictionary(".json")
        dictionary.load_dictionary("data.json")
        self.assertEqual(dictionary.query_dictionary("RAiNn"), ['Precipitation in the form of liquid water drops with '
                                                                'diameters greater than '
                                                                '0.5 millimetres.',
                                                                'To fall from the clouds in drops of water.'])

    def test_query_dictionary_cant_find_it(self):
        """
        Tests if the query does not work if the string passed in to too unrecognizable
        """
        dictionary = Dictionary(".json")
        dictionary.load_dictionary("data.json")
        self.assertFalse(dictionary.query_dictionary("RainnnnnnnnnnnnnPnnnnnnnnnnnnnnnnnnn"))
