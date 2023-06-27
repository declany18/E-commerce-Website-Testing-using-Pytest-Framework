from pages.User_registration_page import UserRegistrationPage
from pages.base_page import BasePage
from utilities.test_data import TestData
from utilities.user_registration_locators import RegistrationLocatorFields


class RegistrationPage(BasePage):
    def __init__(self, driver):
        self.locate = RegistrationLocatorFields
        super().__init__(driver)

    def click_registration_button(self):
        self.click(self.locate.registration_button)
        return UserRegistrationPage(self.driver)

    def set_first_name(self, first_name):
        self.set(self.locate.first_name_field, first_name)

    def set_last_name(self, last_name):
        self.set(self.locate.last_name_field, last_name)

    def set_registration_email(self, new_user_email):
        self.set(self.locate.registration_email_field, new_user_email)

    def set_phone_number(self, phone_number):
        self.set(self.locate.phone_number_field, phone_number)

    def set_password(self, password):
        self.set(self.locate.registration_password_field, password)

    def set_confirm_password(self, confirm_password):
        self.set(self.locate.registration_confirm_password_field, confirm_password)

    def click_checkbox(self):
        self.click(self.locate.privacy_checkbox)

    def Enter_new_user_credentials(self):
        self.click_registration_button()
        self.set_first_name(TestData.first_name)
        self.set_last_name(TestData.last_name)
        self.set_registration_email(TestData.new_user_email)
        self.set_phone_number(TestData.phone)
        self.set_password(TestData.password)
        self.set_confirm_password(TestData.confirm_password)

    def click_continue_button(self):
        self.click(self.locate.continue_button)

    def get_warning_message(self):
        return self.get_text(self.locate.warning_message)

