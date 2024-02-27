import unittest

from pages.login_page import LoginPage

class LoginTests(unittest.TestCase):

    def setUp(self):
        self.login_page = LoginPage()
        self.login_page.open()

    def tearDown(self):
        self.login_page.close()

    def test_login_with_unregistered_email(self):
        self.login_page.set_email("pyta9@gmail.com")
        self.login_page.set_password("12235")
        self.login_page.click_login_button()
        self.login_page.verify_login_error_message("No customer account found")
