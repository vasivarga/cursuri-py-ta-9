from pages.base_page import BasePage


class HomePage(BasePage):

    HOME_PAGE_URL = "https://demo.nopcommerce.com"

    def open(self):
        self.driver.get(self.HOME_PAGE_URL)