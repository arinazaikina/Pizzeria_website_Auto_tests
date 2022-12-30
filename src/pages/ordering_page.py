import logging

import allure
from selenium.common import NoSuchElementException
from selenium.webdriver import Keys

from resource.data_for_testing import TestData
from src.locators.ordering_page_locators import OrderingLocators
from src.pages.base_page import BasePage
from src.utils.utils import get_next_day, get_price


class OrderingPage(BasePage):
    @allure.step('Заполнение поля "Имя"')
    def fill_name_field(self, name: str):
        logging.info('Set name')

        name_field = self.get_visible_element(xpath=OrderingLocators.NAME)
        name_field.clear()
        name_field.send_keys(name)
        value = name_field.get_attribute('value')

        with allure.step(f'Проверка, что значение в поле "Имя" ({value}) равно {name}'):
            assert value == name

        logging.info('Name set')

    @allure.step('Заполнение поля "Фамилия"')
    def fill_surname_field(self, surname: str):
        logging.info('Set surname')
        surname_field = self.get_visible_element(xpath=OrderingLocators.SURNAME)
        surname_field.clear()
        surname_field.send_keys(surname)
        value = surname_field.get_attribute('value')

        with allure.step(f'Проверка, что значение в поле "Фамилия" ({value}) равно {surname}'):
            assert value == surname

        logging.info('Surname set')

    @allure.step('Заполнение поля "Страна"')
    def fill_country_field(self, country: str):
        logging.info('Set country')
        country_select = self.get_visible_element(xpath=OrderingLocators.COUNTRY)
        country_select.click()
        country_input = self.get_visible_element(xpath=OrderingLocators.COUNTRY_INPUT)
        country_input.send_keys(country)
        country_input.send_keys(Keys.ENTER)
        title = country_select.get_attribute('title')

        with allure.step(f'Проверка, что значение в поле "Страна" ({title}) равно {country}'):
            assert title == country

        logging.info('Country set')

    @allure.step('Заполнение поля "Адрес"')
    def fill_address_field(self, address: str):
        logging.info('Set address')

        address_field = self.get_visible_element(xpath=OrderingLocators.ADDRESS)
        address_field.clear()
        address_field.send_keys(address)
        value = address_field.get_attribute('value')

        with allure.step(f'Проверка, что значение в поле "Адрес" ({value}) равно {address}'):
            assert value == address

        logging.info('Address set')

    @allure.step('Заполнение поля "Город"')
    def fill_city_field(self, city: str):
        logging.info('Set city')

        city_field = self.get_visible_element(xpath=OrderingLocators.CITY)
        city_field.clear()
        city_field.send_keys(city)
        value = city_field.get_attribute('value')

        with allure.step(f'Проверка, что значение в поле "Город" ({value}) равно {city}'):
            assert value == city

        logging.info('City set')

    @allure.step('Заполнение поля "Область"')
    def fill_state_field(self, state: str):
        logging.info('Set state')

        state_field = self.get_visible_element(xpath=OrderingLocators.STATE)
        state_field.clear()
        state_field.send_keys(state)
        value = state_field.get_attribute('value')

        with allure.step(f'Проверка, что значение в поле "Область" ({value}) равно {state}'):
            assert value == state

        logging.info('State set')

    @allure.step('Заполнение поля "Почтовый индекс"')
    def fill_postcode_field(self, postcode: str):
        logging.info('Set postcode')

        postcode_field = self.get_visible_element(xpath=OrderingLocators.POSTCODE)
        postcode_field.clear()
        postcode_field.send_keys(postcode)
        value = postcode_field.get_attribute('value')
        with allure.step(f'Проверка, что значение в поле "Почтовый индекс" ({value}) равно {postcode}'):
            assert value == postcode

        logging.info('Postcode set')

    @allure.step('Заполнение поля "Телефон"')
    def fill_phone_field(self, phone: str):
        logging.info('Set postcode')

        phone_field = self.get_visible_element(xpath=OrderingLocators.PHONE)
        phone_field.clear()
        phone_field.send_keys(phone)
        value = phone_field.get_attribute('value')
        with allure.step(f'Проверка, что значение в поле "Телефон" ({value}) равно {phone}'):
            assert value == phone

        logging.info('Phone set')

    @allure.step('Заполнение поля "Адрес почты"')
    def fill_email_field(self, email: str):
        logging.info('Set email')

        email_field = self.get_visible_element(xpath=OrderingLocators.EMAIL)
        email_field.clear()
        email_field.send_keys(email)
        value = email_field.get_attribute('value')
        with allure.step(f'Проверка, что значение в поле "Адрес почты" ({value}) равно {email}'):
            assert value == email

        logging.info('Email set')

    @allure.step('Установка завтрашнего дня в поле "Дата заказа"')
    def fill_date_field(self):
        logging.info('Set next day')

        day, month, year = get_next_day()
        date_field = self.get_visible_element(xpath=OrderingLocators.DATE)
        date_field.click()
        date_field.send_keys(day)
        date_field.send_keys(month)
        date_field.send_keys(year)
        value = date_field.get_attribute('value')
        with allure.step(f'Проверка, что значение в поле "Дата" ({value}) равно {year}-{month}-{day}'):
            assert value == f'{year}-{month}-{day}'

        logging.info('Date set')

    @allure.step('Выбор оплаты при доставке')
    def click_payment_on_delivery(self):
        logging.info('Choice of payment on delivery')

        radio = self.get_visible_element(xpath=OrderingLocators.PAYMENT_ON_DELIVERY)
        radio.click()
        message = self.get_visible_element(xpath=OrderingLocators.MESSAGE_ABOUT_DELIVERY)

        with allure.step('Проверка, что радиобаттон оплаты при доставке активный'):
            assert radio.is_selected()

        with allure.step('Проверка, что появилось сообщение "Оплата наличными при доставке заказа."'):
            assert message.text == 'Оплата наличными при доставке заказа.'

        logging.info('Payment on delivery set')

    @allure.step('Согласие на обработку личных данных')
    def click_on_terms_and_conditions(self):
        logging.info('Click checkbox')

        checkbox = self.get_visible_element(xpath=OrderingLocators.TERMS_AND_CONDITIONS)
        checkbox.click()

        with allure.step('Проверка, что чекбокс согласия активный'):
            assert checkbox.is_selected()

        logging.info('Checkbox active')

    @allure.step('Получение данных по каждой позиции в заказе')
    def get_data_about_all_items_in_the_order(self):
        logging.info('Getting data for each item in the order')

        item_names = self.get_visible_elements(xpath=OrderingLocators.ITEMS_LIST)
        items_list = []
        for name in item_names:
            item_dict = {}

            data_list = name.text.split('×')
            item_name = data_list[0].strip()
            second_part = data_list[1].split('\n')
            price_str = self.get_visible_element(xpath=OrderingLocators.get_total_price_item_locator_by_name(
                item_name=item_name)).text
            price = get_price(price_str)

            item_dict['name'] = item_name
            item_dict['amount'] = int(second_part[0].strip())
            try:
                item_dict['option'] = second_part[2]
            except IndexError:
                item_dict['option'] = None
            item_dict['total_price'] = price

            items_list.append(item_dict)

        logging.info(f"Data for each item is ready {items_list}")

        with allure.step(f'Данные по каждой позиции в заказе: {items_list}'):
            return items_list

    @allure.step('Получение общей стоимости заказа')
    def get_total_cost_order(self):
        logging.info('Getting the total cost of an order')

        total_cost_str = self.get_visible_element(xpath=OrderingLocators.TOTAL_COST).text
        total_cost = get_price(total_cost_str)
        with allure.step(f'Общая стоимость заказа: {total_cost}'):
            logging.info(f'Total = {total_cost}')
            return total_cost

    @allure.step('Получение суммы заказа')
    def get_sum_order(self):
        logging.info('Getting the sum of an order')

        sum_str = self.get_visible_element(xpath=OrderingLocators.SUM).text
        sum_ = get_price(sum_str)
        with allure.step(f'Общая стоимость заказа: {sum_}'):
            logging.info(f'Total = {sum_}')
            return sum_

    @allure.step('Нажатие кнопки оформить заказ')
    def click_checkout(self):
        self.get_visible_element(xpath=OrderingLocators.BUTTON).click()

        logging.info('Button pressed')

    @allure.step('Получение данных по каждой позиции в деталях заказа')
    def get_data_about_all_items_in_the_detail_order(self):
        logging.info('Getting data for each item in the detail_order')

        item_names = self.get_visible_elements(xpath=OrderingLocators.ITEMS_LIST_FOR_DETAIL_ORDER)
        items_list = []
        for name in item_names:
            item_dict = {}
            name = name.text
            amount = int(
                self.get_visible_element(xpath=OrderingLocators.get_amount_item_locator_by_name_for_detail_order(
                                                      item_name=name)).text.split('×')[1].strip())
            sum_str = self.get_visible_element(
                xpath=OrderingLocators.get_total_cost_item_locator_by_name_for_detail_order(
                                                   item_name=name)).text
            sum_ = get_price(sum_str)

            item_dict['name'] = name
            item_dict['amount'] = amount
            item_dict['total_price'] = sum_
            items_list.append(item_dict)

        logging.info(f"Data for each item is ready {items_list}")

        with allure.step(f'Данные по каждой позиции в деталях заказа: {items_list}'):
            return items_list

    @allure.step('Получение общей стоимости в деталях заказа')
    def get_subtotal_order_details(self):
        logging.info('Getting the total cost of an order details')

        subtotal_str = self.get_visible_element(xpath=OrderingLocators.SUBTOTAL).text
        subtotal = get_price(subtotal_str)

        with allure.step(f'Общая стоимость заказа: {subtotal}'):
            logging.info(f'Total = {subtotal}')
            return subtotal

    @allure.step('Получение суммы в деталях заказа')
    def get_total_order_details(self):
        logging.info('Getting the sum of an order details')

        total_str = self.get_visible_element(xpath=OrderingLocators.TOTAL).text
        total = get_price(total_str)

        with allure.step(f'Сумма заказа: {total}'):
            logging.info(f'Total = {total}')
            return total

    @allure.step('Получение способа оплаты')
    def get_payment_method(self):
        logging.info('Getting the payment method an order details')

        payment_method = self.get_visible_element(xpath=OrderingLocators.PAYMENT_METHOD).text

        with allure.step(f'Метод оплаты: {payment_method}'):
            logging.info(f'Payment method = {payment_method}')
            return payment_method

    @allure.step('Получение адреса для отправки чека')
    def get_address_to_a_send_check(self):
        logging.info('Getting address to a send check')

        address = self.get_visible_element(xpath=OrderingLocators.ADDRESS_TO_SEND_A_CHECK).get_attribute('innerHTML'). \
            split('<br>')
        result = {
            'name': address[0].strip().split()[0],
            'surname': address[0].strip().split()[1],
            'street': address[1],
            'city': address[2],
            'state': address[3],
            'postcode': address[4],
            'country': address[5].split('\n')[0],
            'phone': self.get_visible_element(xpath=OrderingLocators.PHONE_IN_ORDER_DETAILS).text,
            'email': self.get_visible_element(xpath=OrderingLocators.EMAIL_IN_ORDER_DETAILS).text
        }

        with allure.step(f'Данные для отправки чека: {result}'):
            logging.info(f'Address = {result}')
            return result

    @allure.step('Открыть поле для ввода купона')
    def show_coupon_field(self):
        logging.info('Open a field for entering a coupon')

        self.get_visible_element(xpath=OrderingLocators.SHOW_COUPON).click()
        field = self.get_visible_element(xpath=OrderingLocators.INPUT_COUPON)
        with allure.step('Проверка, что поле для ввода купона появилось'):
            assert field.is_displayed()

        logging.info('Coupon field is open')

    @allure.step('Заполнение поля для ввода купона')
    def fill_coupon_field(self, code: str):
        logging.info(f'Set code {code}')

        coupon_field = self.get_visible_element(xpath=OrderingLocators.INPUT_COUPON)
        coupon_field.send_keys(code)
        value = coupon_field.get_attribute('value')
        with allure.step(f'Проверка, что значение в поле для ввода купона ({value}) равно {code}'):
            assert value == code

        logging.info(f'Code {code} set')

    @allure.step('Нажатие кнопки "Применить купон"')
    def click_apply_coupon(self):
        self.get_visible_element(xpath=OrderingLocators.APPLY_COUPON).click()

        logging.info('Button pressed')

    @allure.step('Получение сообщения после применения корректного купона')
    def get_message_after_applying_correct_coupon(self):
        message = self.get_visible_element(xpath=OrderingLocators.ALERT).text

        with allure.step(f'Проверка, что появилось сообщение о успешном применении промокода: {message}'):
            assert message == 'Coupon code applied successfully.'

        logging.info(f'Successful coupon application message: {message}')

    @allure.step('Получение сообщения об ошибке после применения некорректного купона')
    def get_message_after_applying_wrong_coupon(self):
        logging.info('Getting error message')
        try:
            message = self.get_element(xpath=OrderingLocators.ERROR_ALERT).text

            with allure.step(f'Проверка, что появилось сообщение об ошибке: {message}'):
                assert message == 'Неверный купон.'

            logging.info(f'Error message: {message}')
            return True

        except NoSuchElementException:
            logging.info('Error message not found')
            return False

    @allure.step('Получение суммы скидки')
    def get_discount_order(self):
        logging.info('Getting the discount of an order')

        try:
            discount_str = self.get_element(xpath=OrderingLocators.DISCOUNT).text
            discount = get_price(discount_str)

            with allure.step(f'Скидка: {discount}'):
                logging.info(f'Discount = {discount}')
                return discount

        except NoSuchElementException:
            logging.info('Discount not found')
            return None

    @allure.step('Получение суммы скидки в деталях заказа')
    def get_discount_details_order(self):
        logging.info('Getting the discount of an details order')

        discount_str = self.get_visible_element(xpath=OrderingLocators.DISCOUNT_ORDER_DETAILS).text
        discount = get_price(discount_str)

        with allure.step(f'Скидка: {discount}'):
            logging.info(f'Discount = {discount}')
            return discount

    @allure.step('Заполнение формы оформления заказа')
    def fill_order_form(self):
        logging.info('Filling out the order form')

        self.fill_name_field(name=TestData.name)
        self.fill_surname_field(surname=TestData.surname)
        self.fill_country_field(country=TestData.country)
        self.fill_address_field(address=TestData.address)
        self.fill_city_field(city=TestData.city)
        self.fill_state_field(state=TestData.state)
        self.fill_postcode_field(postcode=TestData.postcode)
        self.fill_phone_field(phone=TestData.phone)
        self.fill_date_field()
        self.click_payment_on_delivery()
        self.click_on_terms_and_conditions()

        logging.info('Form filled with data')
