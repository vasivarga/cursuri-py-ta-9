import unittest

from pages.register_page import RegisterPage


class RegisterTests(unittest.TestCase):

    def setUp(self):
        self.register_page = RegisterPage()
        self.register_page.open()

    def tearDown(self):
        self.register_page.close()

    def test_register(self):
        self.register_page.set_first_name("PY")
        self.register_page.set_last_name("TA")
        self.register_page.select_birth_day("10")
        self.register_page.select_birth_month("May")
        self.register_page.select_birth_year("1995")
        self.register_page.set_email("pyta9_234234234@gmail.com")
        self.register_page.set_password("pass12345")
        self.register_page.set_password_confirm("pass12345")
        self.register_page.click_register_button()
        self.register_page.verify_success_message_displayed()
        self.register_page.verify_success_message_contains_text("Your registration completed")