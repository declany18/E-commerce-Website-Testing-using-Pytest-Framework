from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class SearchProductPage(BasePage):
    product_search_field = (By.XPATH, "//input[@placeholder='Search For Products']")
    product_search_button = (By.XPATH, "//button[text()='Search']")
    search_value = (By.XPATH, "//h1[contains(text(),'Search')]")

    def __init__(self, driver):
        super().__init__(driver)

    def search_for_product(self, product_name):
        self.set(self.product_search_field, product_name)

    def click_search_button(self):
        self.click(self.product_search_button)

    def get_search_values(self):
        return self.get_text(self.search_value)
