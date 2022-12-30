import logging
import time

import allure

from src.pages.cart_page import CartPage
from src.pages.main_page import MainPage
from src.pages.pizza_page import PizzaPage
from src.utils.utils import get_pizza_names_without_option, get_pizza_names_with_option, get_edited_dict, \
    get_price_by_item_name, get_total_price_by_item_name, get_total_cost_items_in_the_table


@allure.story('Корзина')
@allure.description('Проверка работы опций корзины')
class TestCartPage:
    @allure.title('Кейс id=cart-1: Удаление пиццы с дополнительными опциями из корзины')
    def test_cart_1(self, driver):
        logging.info('Start test_cart-1')

        main_page = MainPage(driver)
        pizza_page = PizzaPage(driver)
        cart_page = CartPage(driver)

        selected_pizzas = []

        main_page.open('http://pizzeria.skillbox.cc/')
        selected_pizzas.append(main_page.add_pizza_to_cart_by_number(position_number=1))
        selected_pizzas.append(main_page.click_pizza_from_the_slider_by_number(position_number=2))

        pizza_page.choose_of_cheese_board()
        pizza_page.add_to_cart()

        cart_page.open('http://pizzeria.skillbox.cc/cart/')
        pizza_names_before_removal = cart_page.get_items_list_in_the_cart()
        data_about_pizza_in_the_cart_before_removal = cart_page.get_data_about_all_items()

        pizza_names_with_option = get_pizza_names_with_option(data_about_pizza_in_the_cart_before_removal)
        for pizza in pizza_names_with_option:
            cart_page.remove_item_by_name(item_name=pizza)
            time.sleep(3)
            message = cart_page.get_message_from_alert()

            with allure.step(f'Проверка, что название пиццы {pizza} есть в сообщении {message}'):
                assert pizza in message

        data_about_pizza_in_the_cart_after_removal = cart_page.get_data_about_all_items()
        pizza_names_without_option = get_pizza_names_without_option(data_about_pizza_in_the_cart_after_removal)

        with allure.step('Проверка, что пицца с опциями удалилась из корзины, а пицца без опций осталась'):
            assert set(pizza_names_without_option) == \
                   set(pizza_names_before_removal).difference(pizza_names_with_option)

        logging.info('Finish test_cart-1')

    @allure.title('Кейс id=cart-2: Изменение количества пиццы в корзине')
    def test_cart_2(self, driver):
        logging.info('Start test_cart-2')

        main_page = MainPage(driver)
        cart_page = CartPage(driver)

        selected_pizzas = []
        main_page.open('http://pizzeria.skillbox.cc/')
        pizza_slider = get_edited_dict(main_page.get_visible_pizzas())
        selected_pizzas.append(main_page.add_pizza_to_cart_by_number(position_number=1))
        selected_pizzas.append(main_page.add_pizza_to_cart_by_number(position_number=3))

        cart_page.open('http://pizzeria.skillbox.cc/cart/')
        data_about_pizza_in_the_cart_before_change = cart_page.get_data_about_all_items()
        for pizza in data_about_pizza_in_the_cart_before_change:
            pizza_name = pizza['name']
            pizza_price = pizza['price']
            with allure.step(f'Проверка корректности цен. {pizza_name} стоит {pizza_slider[pizza_name]}. '
                             f'В корзине указано - {pizza_price}'):
                assert pizza_price == pizza_slider[pizza_name]

        first_pizza_name = data_about_pizza_in_the_cart_before_change[0]['name']
        amount = cart_page.set_amount_by_pizza_name(item_name=first_pizza_name, amount=10)

        data_about_pizza_in_the_cart_after_change = cart_page.get_data_about_all_items()
        price_first_pizza = get_price_by_item_name(data=data_about_pizza_in_the_cart_after_change,
                                                   item_name=first_pizza_name)
        total_price_first_pizza = get_total_price_by_item_name(data=data_about_pizza_in_the_cart_after_change,
                                                               item_name=first_pizza_name)

        with allure.step(f'Проверка, что итоговая стоимость пиццы '
                         f'{first_pizza_name} = {total_price_first_pizza} ({amount} * {price_first_pizza})'):
            assert total_price_first_pizza == price_first_pizza * amount

        total_cost_of_pizzas_in_table = get_total_cost_items_in_the_table(data_about_pizza_in_the_cart_after_change)
        total_cost_in_summary = cart_page.get_total_cost_in_summary()
        with allure.step(f'Проверка, что сумма общей стоимости пицц в таблице ({total_cost_of_pizzas_in_table}) '
                         f'= общей стоимости в сводке ({total_cost_in_summary})'):
            assert total_cost_of_pizzas_in_table == total_cost_in_summary

        logging.info('Finish test_cart-2')
