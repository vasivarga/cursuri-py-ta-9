
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait

from browser import Browser

class BasePage(Browser):

    INPUT_SEARCH = (By.ID, "small-searchterms")
    BUTTON_SEARCH = (By.CLASS_NAME, "search-box-button")
    CART_QUANTITY = (By.CLASS_NAME, "cart-qty")

    def find(self, locator):
        return self.driver.find_element(*locator)

    def type(self, locator, text):
        self.find(locator).send_keys(text)

    def select_dropdown_text(self, locator, text):
        dropdown = Select(self.find(locator))
        dropdown.select_by_visible_text(text)

    def set_search_term(self, text):
        self.type(self.INPUT_SEARCH, text)

    def click_search_button(self):
        self.find(self.BUTTON_SEARCH).click()

    def find_all(self, locator):
        return self.driver.find_elements(*locator)

    def verify_cart_quantity(self, expected):
        expected_text = f'({expected})'
        wait = WebDriverWait(self.driver, 5)
        wait.until(expected_conditions.text_to_be_present_in_element(self.CART_QUANTITY, expected_text))
        assert expected_text in self.find(self.CART_QUANTITY).text



