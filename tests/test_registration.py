from pages.login_page import LoginPage
from pages.registration_page import RegistrationPage
from tests.base_test import BaseTest


class TestRegistration(BaseTest):
    def test_valid_credentials(self):
        registration_page = RegistrationPage(self.driver)
        login_page = LoginPage(self.driver)
        registration_page.Enter_new_user_credentials()
        registration_page.click_checkbox()
        registration_page.click_continue_button()
        actual_title = registration_page.get_title()
        assert actual_title == "Your Account Has Been Created!"

    def test_invalid_unchecked_privacy_checkbox(self):
        login_page = LoginPage(self.driver)
        registration_page = RegistrationPage(self.driver)
        registration_page.Enter_new_user_credentials()
        registration_page.click_continue_button()
        actual_message = registration_page.get_warning_message()
        assert actual_message.__contains__("Warning")


