import logging
import time

import allure

from resource.data_for_testing import TestData
from src.pages.main_page import MainPage
from src.pages.my_account_page import MyAccountPage
from src.pages.navigation import Navigation
from src.pages.ordering_page import OrderingPage
from src.pages.registration_page import RegistrationPage


@allure.story('Сценарии с промокодом')
@allure.description('Проверка работы промокода')
class TestPromo:
    @allure.title('Кейс id=promo-1: Использование актуального промокода')
    def test_promo_1(self, driver):
        logging.info('Start test_promo-1')

        main_page = MainPage(driver)
        navigation = Navigation(driver)
        my_account = MyAccountPage(driver)
        ordering_page = OrderingPage(driver)

        main_page.open('http://pizzeria.skillbox.cc/')
        navigation.click_my_account()
        my_account.authorization(username=TestData.username, password=TestData.password)

        navigation.click_main()
        main_page.add_any_pizza_from_slider_to_cart()
        main_page.click_pagination_button('prev')
        main_page.add_pizza_to_cart_by_number(position_number=1)

        navigation.click_ordering()
        ordering_page.show_coupon_field()
        ordering_page.fill_coupon_field(code=TestData.correct_coupon)
        ordering_page.click_apply_coupon()
        ordering_page.get_message_after_applying_correct_coupon()
        total_cost = ordering_page.get_total_cost_order()
        discount = ordering_page.get_discount_order()
        sum_ = ordering_page.get_sum_order()

        with allure.step(f'Проверка, что скидка составляет 10%. Стоимость заказа = {total_cost}, скидка = {discount}'):
            assert discount == total_cost * 0.1

        with allure.step(f'Проверка, что сумма заказа уменьшилась на размер скидки. Итоговая сума заказа = {sum_}, '
                         f'стоимость заказа до скидки = {total_cost}'):
            assert sum_ == total_cost - discount

        ordering_page.fill_order_form()
        ordering_page.click_checkout()

        discount_details_order = ordering_page.get_discount_details_order()
        total_details_order = ordering_page.get_total_order_details()

        with allure.step(f'Проверка, что скидка в деталях заказа ({discount_details_order}) указана корректно'):
            assert discount == discount_details_order

        with allure.step(f'Проверка, что сумма в деталях заказа ({total_details_order}) указана корректно'):
            assert sum_ == total_details_order

        logging.info('Finish test_promo-1')

    @allure.title('Кейс id=promo-2: Использование неактуального промокода')
    def test_promo_2(self, driver):
        logging.info('Start test_promo-2')

        main_page = MainPage(driver)
        navigation = Navigation(driver)
        my_account = MyAccountPage(driver)
        ordering_page = OrderingPage(driver)

        main_page.open('http://pizzeria.skillbox.cc/')
        navigation.click_my_account()
        my_account.authorization(username=TestData.username, password=TestData.password)

        navigation.click_main()
        main_page.point_to_any_pizza_from_the_slider()
        main_page.click_pagination_button('next')
        time.sleep(1)
        main_page.click_pagination_button('next')
        main_page.add_any_pizza_from_slider_to_cart()

        navigation.click_ordering()
        ordering_page.show_coupon_field()
        ordering_page.fill_coupon_field(code=TestData.wrong_coupon)
        ordering_page.click_apply_coupon()
        ordering_page.get_message_after_applying_wrong_coupon()

        total_cost = ordering_page.get_total_cost_order()
        sum_ = ordering_page.get_sum_order()

        with allure.step(f'Проверка, что скидка не применилась. Общая стоимость {total_cost} = сумме заказа {sum_}'):
            assert sum_ == total_cost

        logging.info('Finish test_promo-2')

    @allure.title('Кейс id=promo-3: Валидация промокода при ошибке на сервере')
    def test_promo_3(self, driver):
        logging.info('Start test_promo-3')

        main_page = MainPage(driver)
        navigation = Navigation(driver)
        my_account = MyAccountPage(driver)
        ordering_page = OrderingPage(driver)

        main_page.open('http://pizzeria.skillbox.cc/')
        navigation.click_my_account()
        my_account.authorization(username=TestData.username, password=TestData.password)

        navigation.click_main()
        main_page.add_any_pizza_from_slider_to_cart()
        navigation.click_ordering()
        ordering_page.show_coupon_field()
        ordering_page.fill_coupon_field(code=TestData.correct_coupon)
        ordering_page.intercept_browser_requests(url='http://pizzeria.skillbox.cc/?wc-ajax=apply_coupon')
        ordering_page.click_apply_coupon()
        time.sleep(5)
        ordering_page.refresh_page()
        discount = ordering_page.get_discount_order()

        with allure.step(f'Проверка, что в итоговой таблице нет строки со скидкой. Скидка = {discount}'):
            assert discount is None

        total_cost = ordering_page.get_total_cost_order()
        sum_ = ordering_page.get_sum_order()

        with allure.step(f'Проверка, что скидка не применилась. Общая стоимость {total_cost} = сумме заказа {sum_}'):
            assert sum_ == total_cost

        logging.info('Finish test_promo-3')

    @allure.title('Кейс id=promo-4: Повторное использование промокода')
    def test_promo_4(self, driver):
        logging.info('Start test_promo-4')

        main_page = MainPage(driver)
        navigation = Navigation(driver)
        reg_page = RegistrationPage(driver)
        ordering_page = OrderingPage(driver)

        username, email = TestData.generate_username_and_email()

        reg_page.open('http://pizzeria.skillbox.cc/register/')
        reg_page.fill_username_field(username=username)
        reg_page.fill_email_field(email=email)
        reg_page.fill_password_field(password=TestData.password)
        reg_page.click_button()
        reg_page.check_for_successful_registration_message()

        navigation.click_main()
        main_page.add_any_pizza_from_slider_to_cart()

        navigation.click_ordering()
        ordering_page.show_coupon_field()
        ordering_page.fill_coupon_field(code=TestData.correct_coupon)
        ordering_page.click_apply_coupon()
        ordering_page.get_message_after_applying_correct_coupon()
        total_cost = ordering_page.get_total_cost_order()
        discount = ordering_page.get_discount_order()
        sum_ = ordering_page.get_sum_order()

        with allure.step(f'Проверка, что скидка составляет 10%. Стоимость заказа = {total_cost}, скидка = {discount}'):
            assert discount == total_cost * 0.1

        with allure.step(f'Проверка, что сумма заказа уменьшилась на размер скидки. Итоговая сума заказа = {sum_}, '
                         f'стоимость заказа до скидки = {total_cost}'):
            assert sum_ == total_cost - discount

        ordering_page.fill_order_form()
        ordering_page.click_checkout()

        discount_details_order = ordering_page.get_discount_details_order()
        total_details_order = ordering_page.get_total_order_details()

        with allure.step(f'Проверка, что скидка в деталях заказа ({discount_details_order}) указана корректно'):
            assert discount == discount_details_order

        with allure.step(f'Проверка, что сумма в деталях заказа ({total_details_order}) указана корректно'):
            assert sum_ == total_details_order

        navigation.click_main()
        main_page.add_any_pizza_from_slider_to_cart()
        navigation.click_ordering()
        ordering_page.show_coupon_field()
        ordering_page.fill_coupon_field(code=TestData.correct_coupon)
        ordering_page.click_apply_coupon()
        ordering_page.get_message_after_applying_wrong_coupon()
        total_cost = ordering_page.get_total_cost_order()
        sum_ = ordering_page.get_sum_order()

        ordering_page.fill_order_form()
        ordering_page.click_checkout()

        with allure.step('Проверка, что появилось сообщение об ошибке'):
            assert ordering_page.get_message_after_applying_wrong_coupon()
        with allure.step(f'Проверка, что скидка не применилась. Общая стоимость {total_cost} = сумме заказа {sum_}'):
            assert sum_ == total_cost

        logging.info('Finish test_promo-4')
