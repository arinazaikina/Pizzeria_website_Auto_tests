import logging

import allure

from src.locators.pizza_page_locators import PizzaPageLocators
from src.pages.base_page import BasePage
from src.utils.utils import get_price


class PizzaPage(BasePage):
    @allure.step('Получение названия пиццы на странице с её описанием')
    def get_pizza_name(self):
        logging.info('Getting the name of the pizza')

        pizza_name = self.get_visible_element(xpath=PizzaPageLocators.PIZZA_NAME).text
        logging.info(f'The name of the pizza is {pizza_name}')

        with allure.step(f'Название пиццы на странице этой пиццы - {pizza_name}'):
            return pizza_name

    @allure.step('Получение цены пиццы на странице с её описанием')
    def get_pizza_price(self):
        logging.info('Getting the price of the pizza')

        pizza_price_str = self.get_visible_element(xpath=PizzaPageLocators.PIZZA_PRICE).text
        pizza_price = get_price(pizza_price_str)
        logging.info(f'The price of the pizza is {pizza_price}')

        with allure.step(f'Цена пиццы на странице этой пиццы: {pizza_price}'):
            return pizza_price

    @allure.step('Выбор обычного борта')
    def choose_of_regular_board(self):
        logging.info('Choice of regular board')

        self.get_visible_element(xpath=PizzaPageLocators.SELECT).click()
        self.get_visible_element(xpath=PizzaPageLocators.REGULAR).click()

        logging.info('Regular board selected')

    @allure.step('Выбор сырного борта')
    def choose_of_cheese_board(self):
        logging.info('Choice of cheese board')

        self.get_visible_element(xpath=PizzaPageLocators.SELECT).click()
        self.get_visible_element(xpath=PizzaPageLocators.CHEESE).click()
        add_price = float(self.get_visible_element(xpath=PizzaPageLocators.CHEESE).get_attribute('value'))
        option_name = self.get_visible_element(xpath=PizzaPageLocators.CHEESE).text.split()[0]
        logging.info('Cheese board selected')

        with allure.step(f'Выбрали {option_name} борт, цена увеличивается на {add_price}'):
            return add_price, f'{option_name} борт'

    @allure.step('Выбор колбасного борта')
    def choose_of_sausage_board(self):
        logging.info('Choice of sausage board')

        self.get_visible_element(xpath=PizzaPageLocators.SELECT).click()
        self.get_visible_element(xpath=PizzaPageLocators.SAUSAGE).click()
        add_price = float(self.get_visible_element(xpath=PizzaPageLocators.SAUSAGE).get_attribute('value'))
        option_name = self.get_visible_element(xpath=PizzaPageLocators.SAUSAGE).text.split()[0]
        logging.info('Sausage board selected')

        with allure.step(f'Выбрали {option_name}, цена увеличивается на {add_price}'):
            return add_price, f'{option_name} борт'

    @allure.step('Добавление пиццы в корзину')
    def add_to_cart(self):
        logging.info('Adding pizza to cart')

        self.get_visible_element(xpath=PizzaPageLocators.ADD_TO_CART).click()

        logging.info('Pizza added')

    @allure.step('Получение сообщения после добавления пиццы в корзину')
    def get_message(self):
        logging.info('Waiting for a message after adding a pizza to the cart')

        message = self.get_visible_element(xpath=PizzaPageLocators.ALERT).text
        logging.info(f'The message ({message}) is received')

        with allure.step(f'Получено сообщение: {message}'):
            return message
