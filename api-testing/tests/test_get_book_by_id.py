import unittest

from requests_folder.simple_books_api import get_book_by_id


class TestGetBookById(unittest.TestCase):

    def test_get_book_by_id(self):
        response = get_book_by_id(1)
        book = response.json()

        self.assertEqual(response.status_code, 200)

        self.assertEqual(book['id'], 1)