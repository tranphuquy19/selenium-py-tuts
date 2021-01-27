import os

import pytest

from selenium import webdriver
from selenium.webdriver.chrome.options import Options


@pytest.yield_fixture(scope='class')
def browser():
    chrome_driver_path = os.path.curdir + '/chromedriver_linux64/chromedriver'
    chrome_options = Options()
    chrome_options.add_argument('--disable-notifications')
    chrome_options.add_argument('--window-size=1600,900')

    driver = webdriver.Chrome(
        executable_path=chrome_driver_path, options=chrome_options)

    yield driver
