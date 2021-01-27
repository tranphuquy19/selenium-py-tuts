from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

from base.selenium_driver import SeleniumDriver

class GoogleSearchPage(SeleniumDriver):
    # Locators
    _input_search = "//input[@title='Tìm kiếm']"
    _btn_search = "(//input[@value='Tìm trên Google'])[2]"

    def __init__(self, driver):
        super().__init__(driver)
        self.waiter = WebDriverWait(driver, 10)

    def get_input_search(self):
        return self.waiter.until(EC.presence_of_element_located((By.XPATH, self._input_search)))

    def get_btn_search(self):
        return self.waiter.until(EC.presence_of_element_located((By.XPATH, self._btn_search)))

    def input_search(self, text):
        input_search = self.waitForElement(self._input_search)
        self.sendKeys(input_search, text, "search_input")

    def click_search(self):
        btn_search = self.waitForElement(self._btn_search)
        self.clickElement(btn_search, "search_button")
