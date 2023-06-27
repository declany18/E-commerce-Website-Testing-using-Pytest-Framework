from pages.edit_account_page import EditAccountPage
from pages.login_page import LoginPage
from tests.base_test import BaseTest
from utilities.test_data import TestData


class TestEditAccount(BaseTest):
    def test_edit_account(self):
        edit_page = EditAccountPage(self.driver)
        login_page = LoginPage(self.driver)
        login_page.set_email_address(TestData.email)
        login_page.set_password(TestData.password)
        login_page.click_login_button()
        edit_page.click_account_edit_button()
        edit_page.enter_first_name(TestData.edit_first_name)
        edit_page.enter_phone_number(TestData.edit_phone)
        edit_page.click_continue_button()
        actual_message = edit_page.get_edit_success_message()
        assert actual_message.__contains__("Success")




