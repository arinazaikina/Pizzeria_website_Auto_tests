import logging

import allure

from src.pages.cart_page import CartPage
from src.pages.main_page import MainPage
from src.pages.menu_page import MenuPage
from src.pages.navigation import Navigation
from src.utils.utils import changes_quotes


@allure.story('Меню сайта')
@allure.description('Выбор десерта с фильтром по цене и добавление его в корзину')
class TestMenuPage:
    @allure.title('Кейс id=menu-1: Выбор десерта с фильтром по цене и добавление его в корзину')
    def test_menu_1(self, driver):
        logging.info('Start test_menu-1')

        main_page = MainPage(driver)
        navigation = Navigation(driver)
        menu_page = MenuPage(driver)
        cart_page = CartPage(driver)

        main_page.open('http://pizzeria.skillbox.cc/')
        navigation.click_submenu_desserts()
        menu_page.setting_the_upper_price_in_the_filter(top_price=135)

        desserts_data = menu_page.get_items_data()
        for item_name in list(desserts_data.keys()):
            with allure.step(f'Проверка, что цена каждой позиции в меню меньше 135 рублей. '
                             f'Позиция - {item_name}, цена {desserts_data[item_name]}'):
                assert desserts_data[item_name] < 135

        with allure.step('Выбор первой позиции в меню'):
            dessert_name = list(desserts_data.keys())[0]
            dessert_price = desserts_data[dessert_name]

        menu_page.add_item_to_cart_by_name(item_name=dessert_name)
        navigation.click_cart()
        dessert_data = cart_page.get_data_about_all_items()[0]
        dessert_name_to_cart = dessert_data['name']
        dessert_price_to_cart = dessert_data['price']

        with allure.step(f'Проверка, что выбранный десерт лежит в корзине. Выбрали - {dessert_name}. '
                         f'В корзине лежит - {dessert_name_to_cart}'):
            assert changes_quotes(dessert_name) == dessert_name_to_cart

        with allure.step(f'Проверка, что цена десерта в корзине ({dessert_price_to_cart}) '
                         f'соответствует цене десерта в меню ({dessert_price}).'):
            assert dessert_price == dessert_price_to_cart

        logging.info('Finish test_menu-1')
