import unittest
import pytest

from pages.google.google_search_page import GoogleSearchPage


@pytest.mark.usefixtures("browser")
class SecondUnitTest(unittest.TestCase):
    @pytest.fixture(autouse=True)
    def setup(self, browser):
        self.driver = browser
        self.driver.get('https://google.com')

    @pytest.mark.order(0)
    def test_wait_for_search_btn(self):
        search_page = GoogleSearchPage(self.driver)
        search_page.input_search('https://doracoder.tk')
        search_page.click_search()
        self.assertEqual(self.driver.title, f'https://doracoder.tk - Tìm trên Google')
