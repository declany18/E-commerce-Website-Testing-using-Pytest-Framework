from pages.login_page import LoginPage
from pages.search_product import SearchProductPage
from tests.base_test import BaseTest
from utilities.test_data import TestData


class TestSearchProduct(BaseTest):

    def test_search_product(self):
        login_page = LoginPage(self.driver)
        search_page = SearchProductPage(self.driver)
        search_page.search_for_product(TestData.product_name)
        search_page.click_search_button()
        actual_product_name = search_page.get_search_values()
        assert "iphone" in actual_product_name
