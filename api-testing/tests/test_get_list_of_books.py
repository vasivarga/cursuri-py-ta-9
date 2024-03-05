import unittest

from requests_folder.simple_books_api import get_list_of_books


class TestGetListOfBooks(unittest.TestCase):

    def test_get_list_of_books_status_code(self):
        response = get_list_of_books()
        self.assertEqual(response.status_code, 200)

    def test_get_list_of_books_number_of_results(self):
        response = get_list_of_books()
        number_of_results = len(response.json())
        self.assertTrue(number_of_results > 5, "Less than 5 results were returned")