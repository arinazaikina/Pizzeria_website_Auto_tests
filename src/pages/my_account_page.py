import logging

import allure

from src.locators.my_account_page_locators import MyAccountLocators
from src.locators.navigation_locators import NavigationLocators
from src.pages.base_page import BasePage


class MyAccountPage(BasePage):
    @allure.step('Проверка логина в приветствии')
    def check_username_in_greeting(self, username: str):
        logging.info('Login verification in greeting')

        greeting = self.get_visible_element(xpath=MyAccountLocators.GREETINGS).text

        with allure.step(f'Проверка, что в приветствии ({greeting}) указан корректный логин {username}'):
            assert username in greeting

        logging.info('Verification completed')

    @allure.step('Нажатие на кнопку "Зарегистрироваться"')
    def click_button_registration(self):
        self.get_visible_element(xpath=MyAccountLocators.REGISTER_BUTTON).click()
        title = self.get_visible_element(xpath=NavigationLocators.SUBTITLE).text

        with allure.step(f'Проверка заголовка страницы. Заголовок = {title}'):
            logging.info('Registration page open')
            assert title == 'Регистрация'

    @allure.step('Авторизация')
    def authorization(self, username: str, password: str):
        logging.info('Authorization start')

        username_field = self.get_visible_element(xpath=MyAccountLocators.USERNAME)
        username_field.send_keys(username)
        value = username_field.get_attribute('value')

        with allure.step(f'Проверка, что значение в поле "Имя пользователя" ({value}) равно {username}'):
            assert value == username

        password_filed = self.get_visible_element(xpath=MyAccountLocators.PASSWORD)
        password_filed.send_keys(password)
        value = password_filed.get_attribute('value')

        with allure.step(f'Проверка, что значение в поле "Пароль" ({value}) равно {password}'):
            assert value == password

        self.get_visible_element(xpath=MyAccountLocators.BUTTON).click()
        self.check_username_in_greeting(username)

        logging.info('Authorization completed')
