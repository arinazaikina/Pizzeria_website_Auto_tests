import logging

import allure

from resource.data_for_testing import TestData
from src.pages.cart_page import CartPage
from src.pages.main_page import MainPage
from src.pages.my_account_page import MyAccountPage
from src.pages.navigation import Navigation
from src.pages.ordering_page import OrderingPage
from src.utils.utils import get_item_names, get_amount_by_item_name, get_total_price_by_item_name, \
    get_option_by_item_name


@allure.story('Оформление заказа')
@allure.description('Проверка работы формы оформления заказа')
class TestOrderingPage:
    @allure.title('Кейс id=ord-1: Оформление заказа')
    def test_ord_1(self, driver):
        logging.info('Start test_ord-1')

        main_page = MainPage(driver)
        navigation = Navigation(driver)
        my_account = MyAccountPage(driver)
        ordering_page = OrderingPage(driver)
        cart_page = CartPage(driver)

        main_page.open('http://pizzeria.skillbox.cc/')
        main_page.add_pizza_to_cart_by_number(position_number=1)
        main_page.add_pizza_to_cart_by_number(position_number=3)

        navigation.click_my_account()
        my_account.authorization(username=TestData.username, password=TestData.password)

        navigation.click_cart()
        items_in_the_cart = cart_page.get_data_about_all_items()
        total_cost_in_the_cart = cart_page.get_total_cost_in_summary()
        sum_in_the_cart = cart_page.get_sum_in_summary()

        navigation.click_ordering()
        ordering_page.fill_name_field(name=TestData.name)
        ordering_page.fill_surname_field(surname=TestData.surname)
        ordering_page.fill_country_field(country=TestData.country)
        ordering_page.fill_address_field(address=TestData.address)
        ordering_page.fill_city_field(city=TestData.city)
        ordering_page.fill_state_field(state=TestData.state)
        ordering_page.fill_postcode_field(postcode=TestData.postcode)
        ordering_page.fill_phone_field(phone=TestData.phone)
        ordering_page.fill_date_field()
        ordering_page.click_payment_on_delivery()
        ordering_page.click_on_terms_and_conditions()

        items_in_the_order = ordering_page.get_data_about_all_items_in_the_order()
        total_cost_in_the_order = ordering_page.get_total_cost_order()
        sum_in_the_order = ordering_page.get_sum_order()

        item_names_in_the_cart = get_item_names(items_in_the_cart)
        item_names_in_the_order = get_item_names(items_in_the_order)

        with allure.step(f'Проверка, что список позиций в корзине соответствует списку позиций в заказе. '
                         f'Корзина: {item_names_in_the_cart} Заказ: {item_names_in_the_order}'):
            assert item_names_in_the_cart == item_names_in_the_order

        for item in item_names_in_the_order:
            amount_item_in_the_cart = get_amount_by_item_name(data=items_in_the_cart, item_name=item)
            amount_item_in_the_order = get_amount_by_item_name(data=items_in_the_order, item_name=item)
            with allure.step(f'Проверка, что количество {item} в корзине соответствует количеству '
                             f'{item} в заказе. Корзина: {amount_item_in_the_cart} Заказ: {amount_item_in_the_order}'):
                assert amount_item_in_the_cart == amount_item_in_the_order

            total_cost_item_in_the_cart = get_total_price_by_item_name(data=items_in_the_cart, item_name=item)
            total_cost_item_in_the_order = get_total_price_by_item_name(data=items_in_the_order, item_name=item)
            with allure.step(f'Проверка, что общая стоимость {item} в корзине соответствует общей стоимости '
                             f'{item} в заказе. Корзина: {total_cost_item_in_the_cart} '
                             f'Заказ: {total_cost_item_in_the_order}'):
                assert total_cost_item_in_the_cart == total_cost_item_in_the_order

            option_item_in_the_cart = get_option_by_item_name(data=items_in_the_cart, item_name=item)
            option_item_in_the_order = get_option_by_item_name(data=items_in_the_order, item_name=item)
            with allure.step(f'Проверка, что опция у {item} в корзине соответствует опции у '
                             f'{item} в заказе. Корзина: {option_item_in_the_cart} Заказ: {option_item_in_the_order}'):
                assert option_item_in_the_cart == option_item_in_the_order

        with allure.step(f'Проверка, что общая стоимость в корзине соответствует общей стоимости '
                         f'в заказе. Корзина: {total_cost_in_the_cart} Заказ: {total_cost_in_the_order}'):
            assert total_cost_in_the_cart == total_cost_in_the_order

        with allure.step(f'Проверка, что сумма в корзине соответствует сумме '
                         f'в заказе. Корзина: {sum_in_the_cart} Заказ: {sum_in_the_order}'):
            assert sum_in_the_cart == sum_in_the_order

        ordering_page.click_checkout()

        items_in_the_details = ordering_page.get_data_about_all_items_in_the_detail_order()
        item_names_in_the_details = get_item_names(items_in_the_details)
        subtotal_in_the_details = ordering_page.get_subtotal_order_details()
        total_in_the_detail = ordering_page.get_total_order_details()

        with allure.step(f'Проверка, что список позиций в заказе соответствует списку позиций в деталях заказа. '
                         f'Заказ: {item_names_in_the_order} Детали: {item_names_in_the_details}'):
            assert item_names_in_the_cart == item_names_in_the_order

        for item in item_names_in_the_details:
            amount_item_in_the_order = get_amount_by_item_name(data=items_in_the_order, item_name=item)
            amount_item_in_the_details = get_amount_by_item_name(data=items_in_the_details, item_name=item)
            with allure.step(f'Проверка, что количество {item} в заказе соответствует количеству '
                             f'{item} в деталях заказа. Заказ: {amount_item_in_the_order} '
                             f'Детали: {amount_item_in_the_details}'):
                assert amount_item_in_the_order == amount_item_in_the_details

            sum_item_in_the_order = get_total_price_by_item_name(data=items_in_the_order, item_name=item)
            sum_item_in_the_details = get_total_price_by_item_name(data=items_in_the_details, item_name=item)
            with allure.step(f'Проверка, что общая стоимость {item} в заказе соответствует общей стоимости '
                             f'{item} в деталях заказа. Заказ: {sum_item_in_the_order} '
                             f'Детали: {sum_item_in_the_details}'):
                assert sum_item_in_the_order == sum_item_in_the_details

        with allure.step(f'Проверка, что общая стоимость в заказе соответствует общей стоимости '
                         f'в деталях. Заказ: {total_cost_in_the_order} Детали: {subtotal_in_the_details}'):
            assert subtotal_in_the_details == total_cost_in_the_order

        with allure.step(f'Проверка, что сумма в заказе соответствует сумме '
                         f'в деталях. Заказ: {sum_in_the_order} Заказ: {total_in_the_detail}'):
            assert sum_in_the_order == total_in_the_detail

        with allure.step('Проверка, что метод оплаты == Оплата при доставке'):
            payment_method = ordering_page.get_payment_method()
            assert payment_method == 'Оплата при доставке'

        address_to_a_send_check = ordering_page.get_address_to_a_send_check()

        with allure.step('Проверка личных данных в деталях заказа'):
            assert address_to_a_send_check['name'] == TestData.name
            assert address_to_a_send_check['surname'] == TestData.surname
            assert address_to_a_send_check['street'] == TestData.address
            assert address_to_a_send_check['city'] == TestData.city
            assert address_to_a_send_check['state'] == TestData.state
            assert address_to_a_send_check['postcode'] == TestData.postcode
            assert address_to_a_send_check['country'] == TestData.country
            assert address_to_a_send_check['phone'] == TestData.phone
            assert address_to_a_send_check['email'] == TestData.email

        logging.info('Finish test_ord-1')
