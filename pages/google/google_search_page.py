from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


class GoogleSearchPage():
    # Locators
    _input_search = "//input[@title='Tìm kiếm']"
    _btn_search = "(//input[@value='Tìm trên Google'])[2]"

    def __init__(self, driver):
        self.driver = driver
        self.waiter = WebDriverWait(driver, 10)

    def get_input_search(self):
        return self.waiter.until(EC.presence_of_element_located((By.XPATH, self._input_search)))

    def get_btn_search(self):
        return self.waiter.until(EC.presence_of_element_located((By.XPATH, self._btn_search)))

    def input_search(self, text):
        self.get_input_search().send_keys(text)

    def click_search(self):
        self.get_btn_search().click()
