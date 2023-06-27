
from selenium.webdriver.common.by import By
from pages.base_page import BasePage
from pages.history_page import HistoryPage


class OrderHistoryPage(BasePage):
    order_history_button = (By.PARTIAL_LINK_TEXT, "Order")

    def __init__(self, driver):
        super().__init__(driver)

    def click_order_history_button(self):
        self.click(self.order_history_button)
        return HistoryPage(self.driver)




