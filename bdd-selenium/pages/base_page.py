from selenium import webdriver
from selenium.webdriver.common.by import By

from browser import Browser


class BasePage(Browser):

    INPUT_SEARCH = (By.ID, "small-searchterms")

    def find(self, locator):
        return self.driver.find_element(*locator)

    def type(self, locator, text):
        self.find(locator).send_keys(text)

    def set_search_term(self, text):
        self.type(self.INPUT_SEARCH, text)

