import logging

import allure

from src.locators.bonus_page_locators import BonusPageLocators
from src.pages.base_page import BasePage


class BonusPage(BasePage):
    @allure.step('Заполнение поля "Имя"')
    def fill_name_field(self, name: str):
        logging.info('Set name')

        name_field = self.get_visible_element(xpath=BonusPageLocators.NAME)
        name_field.send_keys(name)
        value = name_field.get_attribute('value')

        with allure.step(f'Проверка, что значение в поле "Имя" ({value}) равно {name}'):
            assert value == name

        logging.info('Name set')

    @allure.step('Заполнение поля "Телефон"')
    def fill_phone_field(self, phone: str):
        logging.info('Set phone number')

        phone_field = self.get_visible_element(xpath=BonusPageLocators.PHONE)
        phone_field.send_keys(phone)
        value = phone_field.get_attribute('value')

        with allure.step(f'Проверка, что значение в поле "Телефон" ({value}) равно {phone}'):
            assert value == phone

        logging.info('Phone set')

    @allure.step('Нажатие кнопки оформить карту')
    def click_get_card(self):
        self.get_visible_element(xpath=BonusPageLocators.BUTTON_GET_CARD).click()

        logging.info('Button pressed')

    @allure.step('Получение подтверждения об оформлении бонусной карты')
    def get_confirmation(self):
        logging.info('Getting confirmation')

        title = self.get_visible_element(xpath=BonusPageLocators.CONFIRMATION, timeout=60).text

        with allure.step(f'Проверка, что получено подтверждение: {title}'):
            assert title == 'Ваша карта оформлена!'

        logging.info('Confirmation received')

    @allure.step('Получение сообщения об ошибке')
    def get_error_message(self):
        message = self.get_visible_element(xpath=BonusPageLocators.ERROR).text

        logging.info(f'Error message: {message}')
        return message
