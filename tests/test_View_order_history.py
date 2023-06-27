from pages import history_page, order_history_page
from pages.login_page import LoginPage
from tests.base_test import BaseTest
from pages.order_history_page import OrderHistoryPage
from utilities.test_data import TestData


class TestOrderHistory(BaseTest):
    def test_display_order_history(self):
        order_page = OrderHistoryPage(self.driver)
        login_page = LoginPage(self.driver)
        login_page.set_email_address(TestData.email)
        login_page.set_password(TestData.password)
        login_page.click_login_button()
        order_page.click_order_history_button()
        actual_title = order_page.get_title()
        expected_title = "Order History"  # Expected title of the page
        assert actual_title == expected_title, f"Actual title: {actual_title}, Expected title: {expected_title}"




