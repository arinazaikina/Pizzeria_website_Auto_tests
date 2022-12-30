import logging
import random

import allure
from selenium import webdriver

from src.locators.main_page_locators import MainPageLocators
from src.pages.base_page import BasePage
from src.utils.utils import changes_quotes, get_price


class MainPage(BasePage):
    def get_pizzas_list(self):
        pizza_links = self.get_elements(xpath=MainPageLocators.PIZZA_LINK)
        pizza_list = []
        for pizza in pizza_links:
            name = pizza.get_attribute("title")
            if name not in pizza_list:
                pizza_list.append(name)
        return pizza_list

    def get_visible_pizzas(self):
        pizza_links = self.get_visible_elements(xpath=MainPageLocators.ACTIVE_PIZZA)
        pizzas = {}
        for pizza in pizza_links:
            name = pizza.get_attribute("title")
            price_str = self.get_visible_element(xpath=MainPageLocators.get_price_locator(name)).text
            price = get_price(price_str)
            pizzas[name] = price
        return pizzas

    @allure.step('Нажатие на кнопку пагинации')
    def click_pagination_button(self, direction: str):
        logging.info(f'Click {direction}')

        self.get_visible_element(xpath=MainPageLocators.get_direction_button(direction)).click()

    @allure.step('Листание слайдера')
    def slider(self, direction: str):
        logging.info('Checking the slider')

        pizza_amount = len(self.get_pizzas_list())
        current_pizzas = []
        start_visible_pizzas = list(self.get_visible_pizzas().keys())
        count_click = 0
        while current_pizzas != start_visible_pizzas and count_click != pizza_amount:
            visible_pizzas_before_click = list(self.get_visible_pizzas().keys())
            self.point_to_any_pizza_from_the_slider()
            self.click_pagination_button(direction)
            count_click += 1
            visible_pizzas_after_click = list(self.get_visible_pizzas().keys())
            if visible_pizzas_before_click == visible_pizzas_after_click:
                break

            with allure.step('Проверка, что кнопка листания работает корректно. '
                             'Список видимых пицц до клика не равен списку видимых пицц после клика'):
                assert visible_pizzas_before_click != visible_pizzas_after_click

            current_pizzas = visible_pizzas_after_click
        finish_visible_pizzas = list(self.get_visible_pizzas().keys())

        with allure.step('Проверка, что слайдер прошёл круг'):
            assert start_visible_pizzas == finish_visible_pizzas

        logging.info('The slider has completed one lap')

    @allure.step('Выбор любой видимой пиццы из слайдера')
    def random_pizza_name_from_the_slider(self):
        logging.info('Choice of any pizza from the visible ones')

        pizzas_name = list(self.get_visible_pizzas().keys())
        index = random.randrange(len(pizzas_name))
        pizza_name = pizzas_name[index]

        logging.info(f'Selected {pizza_name}')

        with allure.step(f'Выбрана пицца {pizza_name}'):
            return pizza_name

    @allure.step('Наведение указателя мыши на любую пиццу в слайдере')
    def point_to_any_pizza_from_the_slider(self):
        pizza_name = self.random_pizza_name_from_the_slider()
        pizza = self.get_visible_element(xpath=MainPageLocators.get_image_locator_by_pizza_name(pizza_name=pizza_name))
        action_chains = webdriver.ActionChains(self.driver)

        with allure.step(f'Навели указатель мыши на {pizza_name}'):
            action_chains.move_to_element(pizza).perform()

        logging.info(f'Move mouse over {pizza_name}')

    @allure.step('Клик на изображение любой пиццы в слайдере')
    def click_on_any_pizza_from_the_slider(self):
        pizza_name = self.random_pizza_name_from_the_slider()
        pizza = self.get_visible_element(xpath=MainPageLocators.get_image_locator_by_pizza_name(pizza_name=pizza_name))
        action_chains = webdriver.ActionChains(self.driver)
        action_chains.move_to_element(pizza).perform()

        with allure.step(f'Кликнули на изображение {pizza_name}'):
            pizza.click()

        logging.info(f'Clicked on the image {pizza_name}')
        return pizza_name

    @allure.step('Клик на изображение пиццы с определённым порядковым номером в слайдере')
    def click_pizza_from_the_slider_by_number(self, position_number: int):
        logging.info(f'Adding pizza №{position_number} to cart')

        visible_pizzas = list(self.get_visible_pizzas().keys())
        pizza_name = visible_pizzas[position_number - 1]
        pizza = self.get_visible_element(xpath=MainPageLocators.get_image_locator_by_pizza_name(pizza_name=pizza_name))
        action_chains = webdriver.ActionChains(self.driver)
        action_chains.move_to_element(pizza).perform()

        with allure.step(f'Кликнули на изображение {pizza_name}'):
            pizza.click()

        logging.info(f'Clicked on the image {pizza_name}')
        return pizza_name

    @allure.step('Добавление любой пиццы из слайдера в корзину')
    def add_any_pizza_from_slider_to_cart(self):
        pizza_name = self.random_pizza_name_from_the_slider()
        pizza = self.get_visible_element(xpath=MainPageLocators.get_image_locator_by_pizza_name(pizza_name=pizza_name))
        action_chains = webdriver.ActionChains(self.driver)
        action_chains.move_to_element(pizza).perform()

        with allure.step(f'Добавили в корзину {pizza_name}'):
            self.get_visible_element(
                xpath=MainPageLocators.get_cart_locator_by_pizza_name(pizza_name=pizza_name)).click()

        with allure.step('Кнопка "В корзину" изменилась на кнопку "Подробнее"'):
            assert self.get_visible_element(
                xpath=MainPageLocators.get_more_button_locator_by_pizza_name(pizza_name=pizza_name)
            )

        logging.info(f'Added to cart {pizza_name}')
        return changes_quotes(pizza_name)

    @allure.step('Добавление в корзину пиццы с определённым порядковым номером в слайдере')
    def add_pizza_to_cart_by_number(self, position_number: int):
        logging.info(f'Adding pizza №{position_number} to cart')

        visible_pizzas = list(self.get_visible_pizzas().keys())
        pizza_name = visible_pizzas[position_number - 1]
        pizza = self.get_visible_element(xpath=MainPageLocators.get_image_locator_by_pizza_name(pizza_name=pizza_name))
        action_chains = webdriver.ActionChains(self.driver)
        action_chains.move_to_element(pizza).perform()
        self.get_visible_element(xpath=MainPageLocators.get_cart_locator_by_pizza_name(pizza_name=pizza_name)).click()

        with allure.step('Кнопка "В корзину" изменилась на кнопку "Подробнее"'):
            assert self.get_visible_element(
                xpath=MainPageLocators.get_more_button_locator_by_pizza_name(pizza_name=pizza_name)
            )

        logging.info(f'{pizza_name} added to the cart')
        return changes_quotes(pizza_name)
