import unittest

from requests_folder.simple_books_api import submit_order, delete_order, get_order


class TestDeleteOrder(unittest.TestCase):

    def test_delete_order(self):
        book_id = 1
        customer_name = "PYTA9"

        submit_order_response = submit_order(book_id, customer_name)
        order_id = submit_order_response.json()['orderId']

        delete_order_response = delete_order(order_id)
        self.assertTrue(delete_order_response.status_code, 204)

        get_order_response = get_order(order_id)
        expected_error_message = f"No order with id {order_id}."
        print(expected_error_message)
        actual_error_message = get_order_response.json()['error']
        self.assertEqual(expected_error_message, actual_error_message)