import logging

import allure

from src.locators.registration_page_locators import RegistrationLocators
from src.pages.base_page import BasePage


class RegistrationPage(BasePage):
    @allure.step('Заполнение поля "Имя пользователя"')
    def fill_username_field(self, username: str):
        logging.info('Set username')

        username_filed = self.get_visible_element(xpath=RegistrationLocators.USERNAME)
        username_filed.send_keys(username)
        value = username_filed.get_attribute('value')

        with allure.step(f'Проверка, что значение в поле "Имя пользователя" ({value}) равно {username}'):
            assert value == username

        logging.info('Username set')

    @allure.step('Заполнение поля "Адрес почты"')
    def fill_email_field(self, email: str):
        logging.info('Set email')

        email_field = self.get_visible_element(xpath=RegistrationLocators.EMAIL)
        email_field.send_keys(email)
        value = email_field.get_attribute('value')

        with allure.step(f'Проверка, что значение в поле "Адрес почты" ({value}) равно {email}'):
            assert value == email

        logging.info('Email set')

    @allure.step('Заполнение поля "Пароль"')
    def fill_password_field(self, password: str):
        logging.info('Set password')

        password_filed = self.get_visible_element(xpath=RegistrationLocators.PASSWORD)
        password_filed.send_keys(password)
        value = password_filed.get_attribute('value')

        with allure.step(f'Проверка, что значение в поле "Пароль" ({value}) равно {password}'):
            assert value == password

        logging.info('Password set')

    @allure.step('Нажатие на кнопку "Зарегистрироваться"')
    def click_button(self):
        self.get_visible_element(xpath=RegistrationLocators.BUTTON).click()

        logging.info('Button pressed')

    @allure.step('Проверка сообщения об успешной регистрации')
    def check_for_successful_registration_message(self):
        logging.info('Waiting for a successful registration message')

        message = self.get_visible_element(xpath=RegistrationLocators.SUCCESSFUL_REGISTRATION).text
        with allure.step(f'Проверка, что появилось сообщение {message}'):
            assert message == 'Регистрация завершена'

        logging.info(f'The message ({message}) is received. Registration completed')

    @allure.step('Проверка имени пользователя на панели навигации в приветствии')
    def check_username_in_greeting(self, username):
        current_username = self.get_visible_element(xpath=RegistrationLocators.USERNAME_IN_NAVIGATION).text

        with allure.step(f'Ожидаемое имя - {username}. Имя на панели навигации - {current_username}'):
            assert current_username == username

        logging.info('Validation of username in welcome in navigation bar completed')

    @allure.step('Нажатие на имя пользователя в приветствии')
    def click_username_in_greeting(self):
        self.get_visible_element(xpath=RegistrationLocators.USERNAME_IN_NAVIGATION).click()

        logging.info('Clicking on the username in the welcome')

    @allure.step('Получение сообщения об ошибке')
    def get_error_message(self):
        message = self.get_visible_element(xpath=RegistrationLocators.ERROR_MESSAGE).text

        logging.info(f'Error message: {message}')
        return message
