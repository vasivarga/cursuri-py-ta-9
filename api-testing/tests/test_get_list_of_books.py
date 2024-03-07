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

    def test_get_list_of_books_filter_by_type(self):
        response = get_list_of_books(book_type="fiction")

        books = response.json()
        self.assertTrue(response.status_code, 200)

        for book in books:
            book_name = book['name']
            book_type = book['type']
            self.assertEqual(book_type, "fiction", f"Book {book_name} is not of type fiction")

    def test_get_all_books_filter_by_invalid_type(self):
        expected_error_message = "Invalid value for query parameter 'type'. Must be one of: fiction, non-fiction."
        response = get_list_of_books(book_type="horror")

        self.assertEqual(response.status_code, 400, "Unexpected status code")

        actual_error_message = response.json()['error']

        self.assertEqual(expected_error_message, actual_error_message)

    def test_get_all_books_limit_results_valid(self):
        response = get_list_of_books(limit=3)

        self.assertEqual(response.status_code, 200)
        number_of_results = len(response.json())

        self.assertTrue(number_of_results <= 3)


