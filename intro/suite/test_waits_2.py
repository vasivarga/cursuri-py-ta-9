import unittest

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class WaitWhenElementIsNotPresentTests(unittest.TestCase):
    DIV_FINISH = (By.ID, "finish")
    BUTTON_START = (By.XPATH, "//button")

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.get("https://the-internet.herokuapp.com/dynamic_loading/2")

    def tearDown(self):
        self.driver.quit()

    def is_element_present(self, locator):
        lista_elemente_gasite = self.driver.find_elements(*locator)
        return len(lista_elemente_gasite) > 0

    def is_element_absent(self, locator):
        lista_elemente_gasite = self.driver.find_elements(*locator)
        return len(lista_elemente_gasite) == 0

    def test_verify_element_is_not_present(self):
        assert not self.is_element_present(self.DIV_FINISH)
        assert self.is_element_absent(self.DIV_FINISH)

    def test_element_is_displayed_after_loading_finish_implicit_wait(self):
        self.driver.find_element(*self.BUTTON_START).click()
        self.driver.implicitly_wait(15)
        assert self.driver.find_element(*self.DIV_FINISH).is_displayed()
        # self.driver.implicitly_wait(0)
        # self.driver.find_element(By.XPATH, "//input[@id='lalala']")

    def test_element_is_displayed_after_loading_finish_explicit_wait(self):
        self.driver.find_element(*self.BUTTON_START).click()
        wait = WebDriverWait(self.driver, 15)
        wait.until(expected_conditions.presence_of_element_located(self.DIV_FINISH))

        assert self.driver.find_element(*self.DIV_FINISH).is_displayed()
        # self.driver.find_element(By.XPATH, "//input[@id='lalala']")


