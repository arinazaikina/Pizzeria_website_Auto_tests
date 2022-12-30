import logging

import allure

from src.pages.cart_page import CartPage
from src.pages.main_page import MainPage
from src.pages.pizza_page import PizzaPage
from src.utils.utils import changes_quotes, get_item_names, get_option_by_item_name, get_price_by_item_name


@allure.story('Страница пиццы')
@allure.description('Проверка выбора опций для пиццы')
class TestPizzaPage:
    @allure.title('Кейс id=pizza-1: Дополнительные опции к пицце')
    def test_pizza_1(self, driver):
        logging.info('Start test_pizza-1')

        main_page = MainPage(driver)
        pizza_page = PizzaPage(driver)
        main_page.open('http://pizzeria.skillbox.cc/')
        selected_pizza = main_page.click_on_any_pizza_from_the_slider()
        current_pizza = pizza_page.get_pizza_name()

        with allure.step('Сравнение названия выбранной в слайдере пиццы с названием пиццы на открывшейся странице'):
            assert selected_pizza == current_pizza

        regular_price = pizza_page.get_pizza_price()
        pizza_page.choose_of_regular_board()
        price_after_choosing_option = pizza_page.get_pizza_price()

        with allure.step('Проверка того, что при выборе обычного борта цена пиццы не изменилась'):
            assert regular_price == price_after_choosing_option

        add_price, name_option = pizza_page.choose_of_cheese_board()
        price_after_choosing_option = pizza_page.get_pizza_price()

        with allure.step(f'Проверка того, что при выборе сырного борта цена пиццы увеличилась на {add_price}'):
            assert price_after_choosing_option == regular_price + add_price

        add_price, name_option = pizza_page.choose_of_sausage_board()
        price_after_choosing_option = pizza_page.get_pizza_price()

        with allure.step(f'Проверка того, что при выборе колбасного борта цена пиццы увеличилась на {add_price}'):
            assert price_after_choosing_option == regular_price + add_price

        finish_price = price_after_choosing_option
        finish_option = name_option
        pizza_page.add_to_cart()
        message = pizza_page.get_message()

        with allure.step(f'Проверка того, что в сообщении "{message}" указано верное название пиццы - {current_pizza}'):
            assert current_pizza in message

        cart_page = CartPage(driver)
        cart_page.open('http://pizzeria.skillbox.cc/cart/')
        data_about_pizza_in_the_cart = cart_page.get_data_about_all_items()

        pizza_names_in_the_cart = get_item_names(data=data_about_pizza_in_the_cart)
        pizza_option_in_the_cart = get_option_by_item_name(data=data_about_pizza_in_the_cart,
                                                           item_name=changes_quotes(current_pizza))
        pizza_price_in_the_cart = get_price_by_item_name(data=data_about_pizza_in_the_cart,
                                                         item_name=changes_quotes(current_pizza))

        with allure.step(f'В корзине лежит пицца {", ".join(pizza_names_in_the_cart)} с опцией '
                         f'{pizza_option_in_the_cart}. Цена - {pizza_price_in_the_cart}'):
            with allure.step(f'Проверка того, что пицца {current_pizza} лежит в списке пицц корзины.\n'
                             f'Пиццы в корзине: {", ".join(pizza_names_in_the_cart)}'):
                assert changes_quotes(current_pizza) in pizza_names_in_the_cart

            with allure.step(f'Проверка того, что название опции для пиццы корректное - {pizza_option_in_the_cart}'):
                assert finish_option == pizza_option_in_the_cart

            with allure.step(f'Проверка того, что цена пиццы корректная: {pizza_price_in_the_cart}'):
                assert finish_price == pizza_price_in_the_cart

        logging.info('Finish test_pizza-1')
