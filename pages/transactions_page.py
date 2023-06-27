from selenium.webdriver.common.by import By
from pages.base_page import BasePage
from pages.history_page import HistoryPage


class ViewTransactionPage(BasePage):
    transaction_button = (By.PARTIAL_LINK_TEXT, "Transactions")

    def __init__(self, driver):
        super().__init__(driver)

    def click_transactions_button(self):
        self.click(self.transaction_button)
        return HistoryPage(self.driver)
