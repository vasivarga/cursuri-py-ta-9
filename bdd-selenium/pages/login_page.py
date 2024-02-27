from selenium.webdriver.common.by import By

from pages.base_page import BasePage


class LoginPage(BasePage):

    LOGIN_PAGE_URL = "https://demo.nopcommerce.com/login"
    INPUT_EMAIL = (By.ID, "Email")
    INPUT_PASSWORD = (By.ID, "Password")
    BUTTON_LOGIN = (By.CLASS_NAME, "login-button")
    DIV_ERROR_MESSAGE = (By.CLASS_NAME, "message-error")

    def open(self):
        self.driver.get(self.LOGIN_PAGE_URL)

    def verify_url(self):
        assert self.driver.current_url == self.LOGIN_PAGE_URL

    def set_email(self, text):
        self.type(self.INPUT_EMAIL, text)

    def set_password(self, text):
        self.type(self.INPUT_PASSWORD, text)

    def click_login_button(self):
        self.find(self.BUTTON_LOGIN).click()

    # def verify_no_customer_account_found_message(self):
    #     assert "No customer account found" in self.find(self.DIV_ERROR_MESSAGE).text

    def verify_login_error_message(self, text):
        assert text in self.find(self.DIV_ERROR_MESSAGE).text



