from pages.login_page import LoginPage
from pages.transactions_page import ViewTransactionPage
from tests.base_test import BaseTest
from utilities.test_data import TestData


class TestViewTransactions(BaseTest):
    def test_view_transactions(self):
        transaction_page = ViewTransactionPage(self.driver)
        login_page = LoginPage(self.driver)
        login_page.set_email_address(TestData.email)
        login_page.set_password(TestData.password)
        login_page.click_login_button()
        transaction_page.click_transactions_button()
        actual_title = transaction_page.get_title()
        expected_title = "Your Transactions"  # Expected title of the page
        assert actual_title == expected_title, f"Actual title: {actual_title}, Expected title: {expected_title}"
