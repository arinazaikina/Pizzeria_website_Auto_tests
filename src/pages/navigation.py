import logging

import allure
from selenium import webdriver

from src.locators.navigation_locators import NavigationLocators
from src.pages.base_page import BasePage


class Navigation(BasePage):
    @allure.step('Клик по кнопке "ГЛАВНАЯ"')
    def click_main(self):
        logging.info('Clik MAIN')

        self.get_visible_element(xpath=NavigationLocators.MAIN).click()
        sections = self.get_elements(xpath=NavigationLocators.SECTIONS)
        sections_list = []
        for section in sections:
            sections_list.append(section.text)

        with allure.step('Проверка перехода на главную страницу с разделами пицца, десерты, напитки'):
            logging.info('Main page open')
            assert sections_list == ['ПИЦЦА', 'ДЕСЕРТЫ', 'НАПИТКИ']

    @allure.step('Клик по кнопке "МЕНЮ"')
    def click_menu(self):
        logging.info('Clik MENU')

        self.get_visible_element(xpath=NavigationLocators.MENU).click()
        title = self.get_visible_element(xpath=NavigationLocators.PAGE_TITLE).text

        with allure.step(f'Проверка заголовка страницы. Заголовок = {title}'):
            logging.info('Menu page open')
            assert title == 'МЕНЮ'

    @allure.step('Клик по кнопке "ДОСТАВКА И ОПЛАТА"')
    def click_delivery_and_payment(self):
        logging.info('Clik DELIVERY AND PAYMENT')

        self.get_visible_element(xpath=NavigationLocators.DELIVERY_AND_PAYMENT).click()
        title = self.get_visible_element(xpath=NavigationLocators.SUBTITLE).text

        with allure.step(f'Проверка заголовка страницы. Заголовок = {title}'):
            logging.info('Delivery and payment page open')
            assert title == 'Доставка И Оплата'

    @allure.step('Клик по кнопке "АКЦИИ"')
    def click_stock(self):
        logging.info('Clik STOCK')

        self.get_visible_element(xpath=NavigationLocators.STOCK).click()
        title = self.get_visible_element(xpath=NavigationLocators.SUBTITLE).text

        with allure.step(f'Проверка заголовка страницы. Заголовок = {title}'):
            logging.info('Stock page open')
            assert title == 'Акции'

    @allure.step('Клик по кнопке "О НАС"')
    def click_about_us(self):
        logging.info('Clik ABOUT US')

        self.get_visible_element(xpath=NavigationLocators.ABOUT_US).click()
        title = self.get_visible_element(xpath=NavigationLocators.SUBTITLE).text

        with allure.step(f'Проверка заголовка страницы. Заголовок = {title}'):
            logging.info('About us page open')
            assert title == 'О Нас'

    @allure.step('Клик по кнопке "КОРЗИНА"')
    def click_cart(self):
        logging.info('Clik CART')

        self.get_visible_element(xpath=NavigationLocators.CART).click()
        title = self.get_visible_element(xpath=NavigationLocators.SUBTITLE).text

        with allure.step(f'Проверка заголовка страницы. Заголовок = {title}'):
            logging.info('Cart page open')
            assert title == 'Корзина'

    @allure.step('Клик по кнопке "МОЙ АККАУНТ"')
    def click_my_account(self):
        logging.info('Clik MY ACCOUNT')

        self.get_visible_element(xpath=NavigationLocators.MY_ACCOUNT).click()
        title = self.get_visible_element(xpath=NavigationLocators.SUBTITLE).text

        with allure.step(f'Проверка заголовка страницы. Заголовок = {title}'):
            logging.info('My account page open')
            assert title == 'Мой Аккаунт'

    @allure.step('Клик по кнопке "ОФОРМЛЕНИЕ ЗАКАЗА"')
    def click_ordering(self):
        logging.info('Clik ORDERING')

        self.get_visible_element(xpath=NavigationLocators.ORDERING).click()
        title = self.get_visible_element(xpath=NavigationLocators.SUBTITLE).text

        with allure.step(f'Проверка: если корзина пустая, то при клике на оформление заказа осуществится '
                         f'переход в корзину, в противном случае на страницу оформления заказа. Заголовок = {title}'):
            logging.info('Ordering page open')
            assert title == 'Оформление Заказа' or title == 'Корзина'

    @allure.step('Клик по кнопке "БОНУСНАЯ ПРОГРАММА"')
    def click_bonus(self):
        logging.info('Clik BONUS')

        self.get_visible_element(xpath=NavigationLocators.BONUS).click()
        title = self.get_visible_element(xpath=NavigationLocators.SUBTITLE).text

        with allure.step(f'Проверка заголовка страницы. Заголовок = {title}'):
            logging.info('Bonus page open')
            assert title == 'Бонусная Программа'

    @allure.step('Выбор подменю "ПИЦЦА" из меню')
    def click_submenu_pizza(self):
        logging.info('Choice PIZZA from menu')

        menu = self.get_visible_element(xpath=NavigationLocators.MENU)
        action_chains = webdriver.ActionChains(self.driver)
        action_chains.move_to_element(menu).perform()
        self.get_visible_element(xpath=NavigationLocators.SUBMENU_PIZZA).click()
        title = self.get_visible_element(xpath=NavigationLocators.PAGE_TITLE).text

        with allure.step(f'Проверка заголовка страницы. Заголовок = {title}'):
            logging.info('PIZZA MENU page open')
            assert title == 'ПИЦЦА'

    @allure.step('Выбор подменю "ДЕСЕРТЫ" из меню')
    def click_submenu_desserts(self):
        logging.info('Choice DESSERTS from menu')

        menu = self.get_visible_element(xpath=NavigationLocators.MENU)
        action_chains = webdriver.ActionChains(self.driver)
        action_chains.move_to_element(menu).perform()
        self.get_visible_element(xpath=NavigationLocators.SUBMENU_DESSERTS).click()
        title = self.get_visible_element(xpath=NavigationLocators.PAGE_TITLE).text

        with allure.step(f'Проверка заголовка страницы. Заголовок = {title}'):
            logging.info('DESSERTS MENU page open')
            assert title == 'ДЕСЕРТЫ'

    @allure.step('Выбор подменю "НАПИТКИ" из меню')
    def click_submenu_drinks(self):
        logging.info('Choice DRINKS from menu')

        menu = self.get_visible_element(xpath=NavigationLocators.MENU)
        action_chains = webdriver.ActionChains(self.driver)
        action_chains.move_to_element(menu).perform()
        self.get_visible_element(xpath=NavigationLocators.SUBMENU_DRINKS).click()
        title = self.get_visible_element(xpath=NavigationLocators.PAGE_TITLE).text

        with allure.step(f'Проверка заголовка страницы. Заголовок = {title}'):
            logging.info('DRINKS MENU page open')
            assert title == 'НАПИТКИ'
