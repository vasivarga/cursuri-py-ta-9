import unittest

from requests_folder.simple_books_api import submit_order, update_order, get_order


class TestUdateOrder(unittest.TestCase):

    def test_update_order(self):
        book_id = 1
        customer_name = "PYTA9"
        new_customer_name = "Test automation pyta9"

        submit_order_response = submit_order(book_id, customer_name)
        order_id = submit_order_response.json()['orderId']

        update_order_response = update_order(order_id, new_customer_name)

        self.assertEqual(update_order_response.status_code, 204)

        get_order_response = get_order(order_id)
        new_customer_name_response = get_order_response.json()['customerName']

        self.assertEqual(new_customer_name_response, new_customer_name)