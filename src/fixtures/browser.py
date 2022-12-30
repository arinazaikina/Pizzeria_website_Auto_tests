import os.path
import logging

import pytest
from seleniumwire import webdriver
from selenium.webdriver.chrome.service import Service


PATH_TO_CHROMEDRIVER = os.path.join('src', 'resource', 'chromedriver.exe')


@pytest.fixture()
def driver() -> webdriver:
    driver_service = Service(executable_path=PATH_TO_CHROMEDRIVER)
    logging.info('Prepare Chrome browser...')
    driver = webdriver.Chrome(service=driver_service)
    driver.maximize_window()
    logging.info('Browser Chrome has been started')
    yield driver
    driver.quit()
