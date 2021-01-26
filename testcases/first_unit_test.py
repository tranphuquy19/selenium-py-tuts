import os
import unittest

from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


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
        btn_search_locator = "(//input[@value='Tìm trên Google'])[2]"
        input_search_locator = "//input[@title='Tìm kiếm']"
        btn_search = waiter.until(EC.presence_of_element_located((By.XPATH, btn_search_locator)))
        input_search = waiter.until(EC.presence_of_element_located((By.XPATH, input_search_locator)))
        input_search.send_keys("@tranphuquy19")
        btn_search.click()
        self.assertEqual(driver.title, "@tranphuquy19 - Tìm trên Google")

    def test_second_search(self):
        btn_search_locator = "(//input[@value='Tìm trên Google'])[2]"
        input_search_locator = "//input[@title='Tìm kiếm']"
        btn_search = waiter.until(EC.presence_of_element_located((By.XPATH, btn_search_locator)))
        input_search = waiter.until(EC.presence_of_element_located((By.XPATH, input_search_locator)))
        input_search.send_keys("@tranphuquy19")
        btn_search.click()
        self.assertEqual(driver.title, "@tranphuquy19 - Tìm trên Google")

    def tearDown(self):
        driver.quit()


if __name__ == "__main__":
    unittest.main(verbosity=2)
