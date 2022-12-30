import logging

import allure

from resource.data_for_testing import TestData
from src.pages.my_account_page import MyAccountPage
from src.pages.registration_page import RegistrationPage


@allure.story('Регистрация на сайте')
@allure.description('Проверка работы формы регистрации')
class TestRegistrationPage:
    @allure.title('Кейс id=reg-1: Регистрация с новым логином и паролем')
    def test_reg_1(self, driver):
        logging.info('Start test_reg-1')

        reg_page = RegistrationPage(driver)
        my_account_page = MyAccountPage(driver)
        username, email = TestData.generate_username_and_email()
        reg_page.open('http://pizzeria.skillbox.cc/register/')
        reg_page.fill_username_field(username=username)
        reg_page.fill_email_field(email=email)
        reg_page.fill_password_field(password=TestData.password)
        reg_page.click_button()
        reg_page.check_for_successful_registration_message()
        reg_page.check_username_in_greeting(username=username)
        reg_page.click_username_in_greeting()
        my_account_page.check_username_in_greeting(username=username)

        logging.info('Finish test_reg-1')

    @allure.title('Кейс id=reg-2: Регистрация с данными пользователя, который уже был зарегистрирован на сайте')
    def test_reg_2(self, driver):
        logging.info('Start test_reg-2')

        reg_page = RegistrationPage(driver)
        reg_page.open('http://pizzeria.skillbox.cc/register/')
        reg_page.fill_username_field(username=TestData.username)
        reg_page.fill_email_field(email=TestData.email)
        reg_page.fill_password_field(password=TestData.password)
        reg_page.click_button()
        error_message = reg_page.get_error_message()

        with allure.step(f'Проверка, что получено сообщение об ошибке: {error_message}'):
            assert error_message == 'Error: Учетная запись с такой почтой уже зарегистировавана. Пожалуйста ' \
                                    'авторизуйтесь.'

        logging.info('Finish test_reg-1')
