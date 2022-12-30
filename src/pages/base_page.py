import logging

import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait as Wait


class BasePage:
    """
    Базовый класс, описывающий страницу
    """
    def __init__(self, driver):
        self.driver = driver

    @allure.step('Открытие страницы')
    def open(self, url):
        self.driver.get(url)

    def get_visible_element(self, xpath: str, timeout=30):
        """
        Returns a web element by XPATH that is in the DOM and is visible on the page
        """
        return Wait(self.driver, timeout).until(EC.visibility_of_element_located(locator=(By.XPATH, xpath)))

    def get_visible_elements(self, xpath: str, timeout=30):
        """
        Returns a web elements by XPATH that are in the DOM and is visible on the page
        """
        return Wait(self.driver, timeout).until(EC.visibility_of_all_elements_located(locator=(By.XPATH, xpath)))

    def get_element(self, xpath: str):
        """
        Returns an element by XPATH
        """
        self.driver.implicitly_wait(0.5)
        return self.driver.find_element(By.XPATH, xpath)

    def get_elements(self, xpath, timeout=30):
        """
        Returns elements by XPATH
        """
        return Wait(self.driver, timeout).until(EC.presence_of_all_elements_located(locator=(By.XPATH, xpath)))

    def scroll_up(self):
        """
        Scroll to the top of the page
        """
        logging.info('Scrolling')
        self.driver.execute_script("window.scroll(0, 0);")
        logging.info('Finish scrolling')

    def confirm_action(self, timeout=30):
        """
        Confirmation of an action on the page in a pop-up alert
        """
        return Wait(self.driver, timeout).until(EC.alert_is_present()).accept()

    def refresh_page(self):
        """
        Page update
        """
        return self.driver.refresh()

    def intercept_browser_requests(self, url: str):
        """
        Intercept browser requests
        """
        def interceptor(request):
            if request.url == url:
                request.create_response(
                    status_code=500,
                    headers={'Content-Type': 'text/html'},
                    body='Something went wrong...'
                )
        self.driver.request_interceptor = interceptor
