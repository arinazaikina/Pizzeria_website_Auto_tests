import logging

import allure
from selenium import webdriver

from src.locators.menu_page_locators import MenuPageLocators
from src.pages.base_page import BasePage
from src.utils.utils import get_price


class MenuPage(BasePage):

    @allure.step('Получение данных о позициях в меню')
    def get_items_data(self):
        logging.info('Getting data about positions in the menu')

        items_name = self.get_visible_elements(xpath=MenuPageLocators.ITEMS_NAME)
        items = {}
        for item in items_name:
            name = item.text
            price_str = self.get_visible_element(xpath=MenuPageLocators.get_price_item_locator_by_name(name)).text
            price = get_price(price_str)
            items[name] = price

        with allure.step(f'Доступные позиции в меню: {items}'):
            logging.info(f'Menu item data is ready: {items}')
            return items

    @allure.step('Установка верхней границы цены')
    def setting_the_upper_price_in_the_filter(self, top_price: int, step=50):
        logging.info(f'Setting the upper limit of the price is not more than {top_price} rubles')

        current_upper_price_limit_str = self.get_visible_element(xpath=MenuPageLocators.TOP_PRICE).text
        current_upper_price_limit = get_price(current_upper_price_limit_str)
        while current_upper_price_limit > top_price:
            right_button = self.get_visible_element(xpath=MenuPageLocators.RIGHT_BUTTON)
            action_chains = webdriver.ActionChains(self.driver)
            action_chains.click_and_hold(right_button).move_by_offset(xoffset=-step, yoffset=0)
            action_chains.release().perform()
            upper_price_limit_str = self.get_visible_element(xpath=MenuPageLocators.TOP_PRICE).text
            upper_price_limit = get_price(upper_price_limit_str)
            current_upper_price_limit = upper_price_limit

        with allure.step(
                f'Проверка, что после настройки фильтра верхняя цена '
                f'({current_upper_price_limit}) меньше {top_price} руб'):
            assert current_upper_price_limit < top_price

        self.get_visible_element(xpath=MenuPageLocators.SUBMIT_FILTER).click()

        logging.info(f'Upper price limit = {current_upper_price_limit}')

    @allure.step('Добавление позиции меню в корзину')
    def add_item_to_cart_by_name(self, item_name: str):
        with allure.step(f'В корзину добавили: {item_name}'):
            self.get_visible_element(
                xpath=MenuPageLocators.get_to_cart_locator_by_name(item_name=item_name)).click()

        with allure.step('Проверка, что кнопка "В КОРЗИНУ" изменилась на кнопку "ПОДРОБНЕЕ"'):
            assert self.get_visible_element(xpath=MenuPageLocators.get_more_locator_by_name(item_name=item_name))
