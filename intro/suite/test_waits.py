import unittest

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


class WaitWhenElementIsPresentTests(unittest.TestCase):
    DIV_FINISH = (By.ID, "finish")
    BUTTON_START = (By.XPATH, "//button")

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.get("https://the-internet.herokuapp.com/dynamic_loading/1")

    def tearDown(self):
        self.driver.quit()

    def test_verify_element_is_not_displayed(self):
        assert self.driver.find_element(*self.DIV_FINISH).is_displayed() == False

    def test_element_is_displayed_after_loading_finish_implicit_wait(self):
        self.driver.find_element(*self.BUTTON_START).click()
        self.driver.implicitly_wait(15)
        assert self.driver.find_element(*self.DIV_FINISH).is_displayed() == False

    def test_element_is_displayed_after_loading_finish_explicit_wait(self):
        self.driver.find_element(*self.BUTTON_START).click()

        wait = WebDriverWait(self.driver, 15)
        wait.until(EC.visibility_of_element_located(self.DIV_FINISH))

        assert self.driver.find_element(*self.DIV_FINISH).is_displayed()

