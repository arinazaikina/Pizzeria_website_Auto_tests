import logging

import allure

from src.pages.main_page import MainPage
from src.pages.navigation import Navigation


@allure.story('Навигация по сайту')
@allure.description('Проверка корректности работы меню навигации. Проверка возможности перехода из корзины в меню')
class TestNavigation:
    @allure.title('Кейс id=nav-1: Навигация по сайту')
    def test_nav_1(self, driver):
        logging.info('Start test_nav-1')

        main_page = MainPage(driver)
        navigation = Navigation(driver)
        main_page.open('http://pizzeria.skillbox.cc/')
        navigation.click_main()
        navigation.click_menu()
        navigation.click_delivery_and_payment()
        navigation.click_stock()
        navigation.click_about_us()
        navigation.click_my_account()
        navigation.click_ordering()
        navigation.click_bonus()
        navigation.click_cart()
        navigation.click_submenu_desserts()
        navigation.click_submenu_pizza()
        navigation.click_submenu_drinks()

        logging.info('Finish test_nav-1')
