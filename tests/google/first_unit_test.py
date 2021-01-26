import os

import unittest

from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

from pages.google.google_search_page import GoogleSearchPage


class FirstUnitTest(unittest.TestCase):
    def setUp(self):
        global driver, waiter
        chrome_driver_path = os.path.curdir + "/chromedriver_linux64/chromedriver"
        chrome_options = Options()
        chrome_options.add_argument("--disable-notifications")
        chrome_options.add_argument("--window-size=1600,900")

        driver = webdriver.Chrome(
            executable_path=chrome_driver_path, options=chrome_options)
        waiter = WebDriverWait(driver, 10)

        driver.get("https://google.com")

    def test_first_search(self):
        search_page = GoogleSearchPage(driver)
        search_page.input_search("@tranphuquy19")
        search_page.click_search()
        self.assertEqual(driver.title, "@tranphuquy19 - Tìm trên Google")

    def test_second_search(self):
        search_page = GoogleSearchPage(driver)
        search_page.input_search("@tranphuquy19")
        search_page.click_search()
        self.assertEqual(driver.title, "@tranphuquy19 - Tìm trên Google")

    def tearDown(self):
        driver.quit()
