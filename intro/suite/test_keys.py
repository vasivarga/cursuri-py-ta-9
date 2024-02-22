import time
import unittest

from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By


class TestKeys(unittest.TestCase):

    def test_keys(self):
        self.driver = webdriver.Chrome()
        self.driver.get("https://the-internet.herokuapp.com/login")
        input_username = self.driver.find_element(By.ID, "username")

        input_username.send_keys("TomSmith")

        # input_username.send_keys(Keys.ARROW_LEFT)
        # time.sleep(1)
        # input_username.send_keys(Keys.ARROW_LEFT)
        # time.sleep(1)
        # input_username.send_keys(Keys.ARROW_LEFT)
        # time.sleep(1)
        # input_username.send_keys(Keys.ARROW_LEFT)
        # time.sleep(1)
        # input_username.send_keys(Keys.ARROW_LEFT)

        input_username.send_keys(5*Keys.ARROW_LEFT)

        input_username.send_keys("Andrew")
        time.sleep(1)

        print(5*"Ana are mere!")

        assert input_username.get_attribute("value") == "TomAndrewSmith"

        input_username.send_keys(Keys.CONTROL + "A")
        input_username.send_keys(Keys.DELETE)

        assert input_username.get_attribute("value") == ""






