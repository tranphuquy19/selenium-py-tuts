import unittest
import pytest
from selenium.webdriver.support.ui import WebDriverWait
from pages.google.google_search_page import GoogleSearchPage


@pytest.mark.usefixtures("browser")
class FirstUnitTest(unittest.TestCase):
    @pytest.fixture(autouse=True)
    def setup(self, browser):
        self.driver = browser
        self.driver.get('https://google.com')

    @pytest.mark.order(2)
    def test_first_search(self):
        search_page = GoogleSearchPage(self.driver)
        search_page.input_search("@tranphuquy19")
        search_page.click_search()
        self.assertEqual(self.driver.title, f'@tranphuquy19 - Tìm trên Google')

    @pytest.mark.order(1)
    def test_second_search(self):
        search_page = GoogleSearchPage(self.driver)
        search_page.input_search("tranphuquy19@gmail.com")
        search_page.click_search()
        self.assertEqual(self.driver.title, "tranphuquy19@gmail.com - Tìm trên Google")
