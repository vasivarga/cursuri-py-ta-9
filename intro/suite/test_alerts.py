import unittest

from selenium import webdriver
from selenium.webdriver.common.by import By


class TestAlerts(unittest.TestCase):

    BUTTON_JS_ALERT_PROMPT = (By.XPATH, "//button[@onclick='jsPrompt()']")
    P_RESULT = (By.ID, "result")

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.get("https://the-internet.herokuapp.com/javascript_alerts")

    def tearDown(self):
        self.driver.quit()

    def test_accept_alert(self):
        self.driver.find_element(*self.BUTTON_JS_ALERT_PROMPT).click()

        alert = self.driver.switch_to.alert
        alert.accept()

        expected_text = "You entered:"

        actual_text = self.driver.find_element(*self.P_RESULT).text

        # assert expected_text == actual_text
        self.assertEqual(expected_text, actual_text)

    @unittest.skip
    def test_dismiss_alert(self):
        self.driver.find_element(*self.BUTTON_JS_ALERT_PROMPT).click()

        alert = self.driver.switch_to.alert
        alert.dismiss()

        expected_text = "You entered: null"

        actual_text = self.driver.find_element(*self.P_RESULT).text

        # assert expected_text == actual_text
        self.assertEqual(expected_text, actual_text)

    def test_accept_alert_with_text(self):
        self.driver.find_element(*self.BUTTON_JS_ALERT_PROMPT).click()

        alert = self.driver.switch_to.alert
        string = "pyta9"

        alert.send_keys(string)
        alert.accept()

        expected_text = "You entered: " + string

        actual_text = self.driver.find_element(*self.P_RESULT).text

        # assert expected_text == actual_text
        self.assertEqual(expected_text, actual_text)

