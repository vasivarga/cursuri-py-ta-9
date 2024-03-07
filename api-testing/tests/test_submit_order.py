import unittest

from requests_folder.simple_books_api import submit_order


class TestSubmitOrder(unittest.TestCase):

    def test_submit_valid_order(self):
        book_id = 1
        customer_name = "PYTA9"

        response = submit_order(book_id, customer_name)

        self.assertEqual(response.status_code, 201, "Unexpected status code")

        is_created = response.json()['created']

        self.assertTrue(is_created)

    def test_submit_order_with_invalid_book_id(self):
        response = submit_order(20, "PYTA9")
        expected_error_message = "Invalid or missing bookId."

        actual_error_message = response.json()['error']

        self.assertEqual(expected_error_message, actual_error_message)