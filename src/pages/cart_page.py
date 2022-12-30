import logging
import time

import allure
from selenium.common import TimeoutException

from src.locators.cart_page_locators import CartPageLocators
from src.pages.base_page import BasePage
from src.utils.utils import get_price


class CartPage(BasePage):
    @allure.step('Получение списка позиций в корзине')
    def get_items_list_in_the_cart(self):
        logging.info('Getting a list of items in the cart')

        item_names = self.get_visible_elements(xpath=CartPageLocators.ITEM_LIST)
        item_names_list = []
        for name in item_names:
            item_names_list.append(name.text)

        logging.info(f'The list of items in the cart is ready: {", ".join(item_names_list)}')

        with allure.step(f'Список позиций в корзине: {", ". join(item_names_list)}'):
            return item_names_list

    @allure.step('Получение данных по каждой позиции в корзине')
    def get_data_about_all_items(self):
        logging.info('Getting data for each item in the cart')

        item_names = self.get_items_list_in_the_cart()
        item_list = []
        for item_name in item_names:
            item_dict = {}
            price_str = self.get_visible_element(xpath=CartPageLocators.get_price_locator_by_item_name(
                item_name=item_name)).text
            price = get_price(price_str)
            amount = int(self.get_visible_element(xpath=CartPageLocators.get_amount_locator_by_item_name(
                item_name=item_name)).get_attribute('value'))
            total_price_str = self.get_visible_element(xpath=CartPageLocators.get_total_price_locator_by_item_name(
                item_name=item_name)).text
            total_price = get_price(total_price_str)
            try:
                option = self.get_visible_element(xpath=CartPageLocators.get_option_locator_by_item_name(
                    item_name=item_name), timeout=1).text
            except TimeoutException:
                option = None
            item_dict['name'] = item_name
            item_dict['price'] = price
            item_dict['amount'] = amount
            item_dict['total_price'] = total_price
            item_dict['option'] = option
            item_list.append(item_dict)

        logging.info(f"Data for each item is ready {item_list}")

        with allure.step(f'Данные по каждой позиции в корзине: {item_list}'):
            return item_list

    @allure.step('Удаление позиции из корзины по названию')
    def remove_item_by_name(self, item_name: str):
        logging.info(f'{item_name} removal')

        with allure.step(f'Удаление позиции {item_name}'):
            self.get_visible_element(xpath=CartPageLocators.get_delete_locator_by_item_name(
                item_name=item_name)).click()

        time.sleep(2)
        self.scroll_up()

    @allure.step('Получение сообщения об обновлении корзины')
    def get_message_from_alert(self):
        message = self.get_visible_element(xpath=CartPageLocators.ALERT, timeout=30).text

        with allure.step(f'Получено сообщение: {message}'):
            logging.info(f'Alert: {message}')
            return message

    @allure.step('Изменение количества позиции')
    def set_amount_by_pizza_name(self, item_name: str, amount: int):
        logging.info(f'Setting number of {item_name} = {amount}')

        field = self.get_visible_element(xpath=CartPageLocators.get_amount_locator_by_item_name(item_name=item_name))
        field.clear()
        field.send_keys(amount)
        current_amount = int(field.get_attribute('value'))

        with allure.step(f'Проверка, что установлено требуемое значение. Требуемое значение = {amount}. '
                         f'Установленное значение = {current_amount}'):
            assert current_amount == amount

        self.get_visible_element(xpath=CartPageLocators.UPDATE_CART).click()
        message = self.get_message_from_alert()

        with allure.step(f'Получено сообщение: {message}'):
            logging.info(f'Alert: {message}')
            assert message == 'Cart updated.'

        return amount

    @allure.step('Получение общей стоимости позиций в корзине')
    def get_total_cost_in_summary(self):
        total_cost_str = self.get_visible_element(xpath=CartPageLocators.TOTAL_COST_IN_SUMMARY).text
        total_cost = get_price(total_cost_str)

        with allure.step(f'Общая стоимость позиций в корзине = {total_cost}'):
            logging.info(f'Total cost of items in the cart: {total_cost}')
            return total_cost

    @allure.step('Получение суммы в корзине')
    def get_sum_in_summary(self):
        sum_str = self.get_visible_element(xpath=CartPageLocators.SUM_IN_SUMMARY).text
        sum_ = get_price(sum_str)

        with allure.step(f'Общая сумма в корзине = {sum_}'):
            logging.info(f'Sum in the cart: {sum_}')
            return sum_

    @allure.step('Нажатие на кнопку "Перейти к оплате"')
    def click_go_to_the_payment(self):
        self.get_visible_element(xpath=CartPageLocators.GO_TO_THE_PAYMENT).click()

        logging.info('Button pressed to proceed to payment')
