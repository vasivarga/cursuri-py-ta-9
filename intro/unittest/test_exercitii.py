import unittest

from selenium import webdriver
from selenium.webdriver.common.by import By


class LoginTests(unittest.TestCase):

    # Declaram locatorii sub forma de tuplu ca sa nu le re-declaram mereu in teste
    # Numele variabilelor le-am scris cu litera mare pt ca sunt constante
    INPUT_EMAIL = (By.ID, "Email")
    INPUT_PASSWORD = (By.ID, "Password")
    BUTTON_LOGIN = (By.CLASS_NAME, "login-button")
    ERROR_LOGIN = (By.CLASS_NAME, "message-error")
    ERROR_EMAIL = (By.ID, "Email-error")

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.get("https://demo.nopcommerce.com/login")
        self.driver.maximize_window()

    def tearDown(self):
        self.driver.quit()

    # Medtoda ajutatoare care cauta si returneaza un WebElement dupa un locator dat
    # Despachetarea tuplului (cu steluta) se intampla in interiorul metodei
    def find(self, locator):
        #Tuplul va fi despachetat deoarece metoda find_element() primeste 2 argumente
        return self.driver.find_element(*locator)

    # Metoda ajutatoare care scrie pe un element
    def type(self, locator, text):
        self.find(locator).send_keys(text)

    # Metoda ajutatoare pt click pe un element
    def click(self, locator):
        self.find(locator).click()

    def test_login_with_unregistered_email_address(self):
        self.type(self.INPUT_EMAIL, "pyta9@gmail.com")
        self.type(self.INPUT_PASSWORD, "1345678945")
        self.click(self.BUTTON_LOGIN)

        # assert self.driver.find_element(By.CLASS_NAME, "message-error").is_displayed(), "Login error not displayed"
        self.assertTrue(self.find(self.ERROR_LOGIN).is_displayed(), "Login error not displayed")

        text_expected = "Login was unsuccessful. Please correct the errors and try again.\nNo customer account found"
        text_actual = self.find(self.ERROR_LOGIN).text
        self.assertEqual(text_expected, text_actual)

    def test_invalid_email_format(self):
        self.type(self.INPUT_EMAIL, "pyta9")
        self.click(self.INPUT_PASSWORD)

        self.assertTrue(self.find(self.ERROR_EMAIL).is_displayed(), "Email error not displayed")
        text_actual = self.find(self.ERROR_EMAIL).text
        text_expected = "Wrong email"
        self.assertEqual(text_expected, text_actual, "Email error message not displayed")