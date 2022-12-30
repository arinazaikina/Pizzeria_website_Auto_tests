import logging

import allure

from resource.data_for_testing import TestData
from src.pages.bonus_page import BonusPage
from src.pages.main_page import MainPage
from src.pages.navigation import Navigation
from src.utils.utils import get_status_phone_number


@allure.story('Сценарии с бонусной системой')
@allure.description('Проверка работы бонусной системы')
class TestPromo:
    @allure.title('Кейс id=bonus-1: Успешное оформление бонусной карты при вводе корректного имени и '
                  'корректного российского номера телефона')
    def test_bonus_1(self, driver):
        logging.info('Start test_bonus-1')

        main_page = MainPage(driver)
        navigation = Navigation(driver)
        bonus_page = BonusPage(driver)

        main_page.open('http://pizzeria.skillbox.cc/')
        navigation.click_bonus()
        bonus_page.fill_name_field(name=TestData.name_bonus)
        bonus_page.fill_phone_field(phone=TestData.phone_bonus)
        bonus_page.click_get_card()
        bonus_page.confirm_action()
        bonus_page.get_confirmation()

        logging.info('Finish test_bonus-1')

    @allure.title('Кейс id=bonus-2: Нажатие "Оформить карту" при пустых обязательных полях')
    def test_bonus_2(self, driver):
        logging.info('Start test_bonus-2')

        main_page = MainPage(driver)
        navigation = Navigation(driver)
        bonus_page = BonusPage(driver)

        main_page.open('http://pizzeria.skillbox.cc/')
        navigation.click_bonus()
        bonus_page.click_get_card()
        error_message = bonus_page.get_error_message()

        with allure.step(f'Проверка, что получено сообщение об ошибке: {error_message}'):
            assert error_message == 'Поле "Имя" обязательно для заполнения\nПоле "Телефон" обязательно для заполнения'

        logging.info('Finish test_bonus-2')

    @allure.title('Кейс id=bonus-3: Поле Имя принимает латиницу, кириллицу, цифры')
    def test_bonus_3(self, driver):
        logging.info('Start test_bonus-3')

        main_page = MainPage(driver)
        navigation = Navigation(driver)
        bonus_page = BonusPage(driver)

        main_page.open('http://pizzeria.skillbox.cc/')
        navigation.click_bonus()
        bonus_page.fill_name_field(name=TestData.name_bonus_different_symbols)
        bonus_page.fill_phone_field(phone=TestData.phone_bonus)
        bonus_page.click_get_card()
        bonus_page.confirm_action()
        bonus_page.get_confirmation()

        logging.info('Finish test_bonus-3')

    @allure.title('Кейс id=bonus-4: Поле Телефон не принимает некорректные номера')
    def test_bonus_4(self, driver):
        logging.info('Start test_bonus-4')

        main_page = MainPage(driver)
        navigation = Navigation(driver)
        bonus_page = BonusPage(driver)

        main_page.open('http://pizzeria.skillbox.cc/')
        navigation.click_bonus()
        for phone_number in TestData.wrong_phone_numbers:
            bonus_page.fill_name_field(name=TestData.name)
            status_phone_number = get_status_phone_number(phone_number=phone_number)
            bonus_page.fill_phone_field(phone=phone_number)
            bonus_page.click_get_card()
            message = bonus_page.get_error_message()

            with allure.step(f'Проверка, что номер телефона {phone_number} не корректный'):
                assert not status_phone_number

            with allure.step(f'Проверка, что появилось сообщение об ошибке: {message}'):
                assert message == 'Введен неверный формат телефона'

            bonus_page.refresh_page()

        logging.info('Finish test_bonus-4')
