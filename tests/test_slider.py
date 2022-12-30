import logging

import allure

from src.pages.cart_page import CartPage
from src.pages.main_page import MainPage


@allure.story('Главная страница сайта')
@allure.description('Проверка работы слайдера')
class TestMainPage:
    @allure.title('Кейс id=slider-1: Пагинация в слайдере')
    def test_slider_1(self, driver):
        logging.info('Start test_slider-1')

        main_page = MainPage(driver)
        main_page.open('http://pizzeria.skillbox.cc/')
        with allure.step('Листание слайдера вправо'):
            main_page.slider('next')
        with allure.step('Листание слайдера влево'):
            main_page.slider('prev')

        logging.info('Finish test_slider-1')

    @allure.title('Кейс id=slider-2: Добавление пиццы в корзину из слайдера')
    def test_slider_2(self, driver):
        logging.info('Start test_slider-2')

        selected_pizzas = []
        main_page = MainPage(driver)
        main_page.open('http://pizzeria.skillbox.cc/')
        with allure.step('Добавление в корзину первой пиццы из слайдера'):
            selected_pizzas.append(main_page.add_pizza_to_cart_by_number(position_number=1))
        with allure.step('Добавление в корзину последней пиццы из слайдера'):
            selected_pizzas.append(main_page.add_pizza_to_cart_by_number(position_number=4))
        with allure.step('Листание слайдера вправо на один шаг'):
            main_page.click_pagination_button('next')
        with allure.step('Добавление в корзину последней пиццы из слайдера'):
            selected_pizzas.append(main_page.add_pizza_to_cart_by_number(position_number=4))
        with allure.step('Переход в корзину'):
            cart_page = CartPage(driver)
            cart_page.open('http://pizzeria.skillbox.cc/cart/')
        pizzas_in_cart = cart_page.get_items_list_in_the_cart()
        with allure.step(f'Сравнение списка выбранных пицц со списком пицц в корзине.\n'
                         f'Выбранные пиццы: {", ".join(selected_pizzas)}\n'
                         f'Пиццы в корзине: {", ".join(pizzas_in_cart)}'):
            assert selected_pizzas == pizzas_in_cart

        logging.info('Finish test_slider-2')
