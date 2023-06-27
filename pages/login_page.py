from utilities.login_locators import LoginLocatorFields
from pages.base_page import BasePage
from pages.my_account_page import MyAccountPage


class LoginPage(BasePage):

    def __init__(self, driver):
        self.locate = LoginLocatorFields
        super().__init__(driver)

    def set_email_address(self, email_address):
        self.set(self.locate.email_address_field, email_address)
        # self.driver.find_element(self.email_address_field).send_keys(email_address)

    def set_password(self, password):
        self.set(self.locate.password_field, password)

    def click_login_button(self):
        self.click(self.locate.login_button)
        return MyAccountPage(self.driver)

    def log_into_application(self, email, password):
        self.set_email_address(email)
        self.set_password(password)
        self.click_login_button()

    def get_warning_message(self):
        return self.get_text(self.locate.warning_message)
