import string
import random


class TestData:
    username = 'sav'
    email = 'sav@test.ru'
    password = 'qwerty'
    name = 'Arina'
    surname = 'Zaikina'
    country = 'Georgia'
    address = 'Ana Politkovskaia Street, 12'
    city = 'Tbilisi'
    state = 'Tbilisi'
    postcode = '123456'
    phone = '+995 123 456 789'
    correct_coupon = 'GIVEMEHALYAVA'
    wrong_coupon = 'DC120'
    name_bonus = 'Арина'
    phone_bonus = '89219999999'
    name_bonus_different_symbols = 'ТестTest12345'
    wrong_phone_numbers = ['+995 123 456 789', '1234567889012334', '1234qwerty', '99877766789']

    @classmethod
    def generate_username_and_email(cls):
        letters_and_digits = string.ascii_letters + string.digits
        rand_string = ''.join(random.sample(letters_and_digits, 10))
        name = rand_string
        email = f'{name}@test.ru'
        return name, email
