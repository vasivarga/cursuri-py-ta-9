from selenium.webdriver.common.by import By

from pages.base_page import BasePage


class SearchResultsPage(BasePage):

    PRODUCT_TITLE = (By.CLASS_NAME, "product-title")
    BUTTOB_ADD_TO_CART = (By.CLASS_NAME, "product-box-add-to-cart-button")

    def verify_url(self):
        assert "https://demo.nopcommerce.com/search?q=" in self.driver.current_url

    def verify_search_results_displayed(self):
        results = self.find_all(self.PRODUCT_TITLE)
        assert len(results) > 0

    def click_add_to_cart(self):
        self.find(self.BUTTOB_ADD_TO_CART).click()