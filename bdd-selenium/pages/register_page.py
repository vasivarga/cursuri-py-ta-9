import random

from selenium.webdriver.common.by import By

from pages.base_page import BasePage


class RegisterPage(BasePage):
    INPUT_FIRST_NAME = (By.ID, "FirstName")
    INPUT_LAST_NAME = (By.ID, "LastName")
    SELECT_BIRTH_DAY = (By.NAME, "DateOfBirthDay")
    SELECT_BIRTH_MONTH = (By.NAME, "DateOfBirthMonth")
    SELECT_BIRTH_YEAR = (By.NAME, "DateOfBirthYear")
    INPUT_EMAIL = (By.ID, "Email")
    INPUT_PASSWORD = (By.ID, "Password")
    INPUT_PASSWORD_CONFIRM = (By.ID, "ConfirmPassword")
    BUTTON_REGISTER = (By.ID, "register-button")
    MESSAGE_SUCCESS = (By.CLASS_NAME, "result")
    REGISTER_PAGE_URL = "https://demo.nopcommerce.com/register"

    ERROR_FIRST_NAME = (By.ID, "FirstName-error")
    ERROR_LAST_NAME = (By.ID, "LastName-error")
    ERROR_EMAIL = (By.ID, "Email-error")
    ERROR_PASSWORD = (By.ID, "Password-error")
    ERROR_CONFIRM_PASSWORD = (By.ID, "ConfirmPassword-error")

    def open(self):
        self.driver.get(self.REGISTER_PAGE_URL)

    def set_first_name(self, first_name):
        self.type(self.INPUT_FIRST_NAME, first_name)

    def set_last_name(self, last_name):
        self.type(self.INPUT_LAST_NAME, last_name)

    def select_birth_day(self, text):
        self.select_dropdown_text(self.SELECT_BIRTH_DAY, text)

    def select_birth_month(self, text):
        self.select_dropdown_text(self.SELECT_BIRTH_MONTH, text)

    def select_birth_year(self, text):
        self.select_dropdown_text(self.SELECT_BIRTH_YEAR, text)

    def set_unique_email(self):
        number = random.randint(0, 9999999999999999)
        email_address = f"pyta9_{number}@gmail.com"
        self.set_email(email_address)

    def set_email(self, text):
        self.type(self.INPUT_EMAIL, text)

    def set_password(self, text):
        self.type(self.INPUT_PASSWORD, text)

    def set_password_confirm(self, text):
        self.type(self.INPUT_PASSWORD_CONFIRM, text)

    def click_register_button(self):
        self.find(self.BUTTON_REGISTER).click()

    def verify_success_message_displayed(self):
        assert self.find(self.MESSAGE_SUCCESS).is_displayed(), "Success message is not displayed!"

    def verify_success_message_contains_text(self, text):
        assert self.find(self.MESSAGE_SUCCESS).text == text, "Success message is not correct!"

    def verify_url(self):
        assert self.driver.current_url == self.REGISTER_PAGE_URL

    def verify_first_name_error_displayed(self):
        assert self.find(self.ERROR_FIRST_NAME).is_displayed()

    def verify_last_name_error_displayed(self):
        assert self.find(self.ERROR_LAST_NAME).is_displayed()

    def verify_email_error_displayed(self):
        assert self.find(self.ERROR_EMAIL).is_displayed()

    def verify_password_error_displayed(self):
        assert self.find(self.ERROR_PASSWORD).is_displayed()

    def verify_password_confirm_error_displayed(self):
        assert self.find(self.ERROR_CONFIRM_PASSWORD).is_displayed()