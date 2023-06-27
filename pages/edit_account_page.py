from selenium.webdriver.common.by import By
from pages.base_page import BasePage
from pages.history_page import HistoryPage


class EditAccountPage(BasePage):
    edit_button = (By.PARTIAL_LINK_TEXT, "Edit Account")
    first_name_edit_field = (By.ID, "input-firstname")
    phone_number_edit_field = (By.ID, "input-telephone")
    continue_button = (By.XPATH, "//*[@id='content']/form/div/div[2]/input")
    edit_success_message = (By.CSS_SELECTOR, "#account-account .alert-success")

    def __init__(self, driver):
        super().__init__(driver)

    def click_account_edit_button(self):
        self.click(self.edit_button)
        return HistoryPage(self.driver)

    def enter_first_name(self, edit_first_name):
        self.set(self.first_name_edit_field, edit_first_name)

    def enter_phone_number(self, edit_phone):
        self.set(self.phone_number_edit_field, edit_phone)

    def click_continue_button(self):
        self.click(self.continue_button)

    def get_edit_success_message(self):
        return self.get_text(self.edit_success_message)
