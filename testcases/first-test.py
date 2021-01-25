import os

from selenium import webdriver
from selenium.webdriver.chrome.options import Options

chrome_driver_path = os.path.curdir + '/chromedriver_linux64/chromedriver'
chrome_options = Options()
chrome_options.add_argument('--disable-notifications')
chrome_options.add_argument("--window-size=1600,900")

driver = webdriver.Chrome(
    executable_path=chrome_driver_path, chrome_options=chrome_options)

driver.get('https://google.com')

print('done')
