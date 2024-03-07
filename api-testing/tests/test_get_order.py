import unittest

from requests_folder.simple_books_api import submit_order, get_order


class TestGetOrder(unittest.TestCase):

    def test_get_order(self):
        book_id = 1
        customer_name = "PYTA9"

        submit_order_response = submit_order(book_id, customer_name)
        order_id = submit_order_response.json()['orderId']

        get_order_response = get_order(order_id)

        self.assertEqual(get_order_response.status_code, 200)

        order_id_response = get_order_response.json()['id']
        customer_name_response = get_order_response.json()['customerName']
        self.assertTrue(order_id_response, order_id)
        self.assertTrue(customer_name_response, customer_name)