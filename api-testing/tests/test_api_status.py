import unittest

from requests_folder.simple_books_api import get_api_status


class TestApiStatus(unittest.TestCase):

    def test_api_status_code_and_body(self):
        response = get_api_status()

        expected_status_code = 200
        actual_status_code = response.status_code

        # assert expected_status_code == actual_status_code, "Unexpected status code"
        self.assertEqual(expected_status_code, actual_status_code, "Unexpected status code")

        body = response.json()

        # assert body["status"] == "OK"
        self.assertEqual(body["status"], "OK", "Unexpected api status")