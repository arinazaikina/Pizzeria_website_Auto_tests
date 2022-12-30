from datetime import date, timedelta, datetime
import re
from typing import List, Dict


def changes_quotes(data: str) -> str:
    """
    Replace quotes «» with ""
    """
    for symbol in ['«', '»']:
        if symbol in data:
            data = data.replace(symbol, '"')
    return data


def get_item_names(data: List[Dict]) -> List[str]:
    """
    Returns a list of values from dictionaries by key 'name'
    """
    item_names = []
    for item_dict in data:
        item_names.append(item_dict['name'])
    return item_names


def get_price_by_item_name(data: List[Dict], item_name: str) -> str:
    """
    Returns a value by key 'price' from a dictionary whose value by key 'name' is equal to item_name
    """
    for item_dict in data:
        if item_dict['name'] == item_name:
            return item_dict['price']


def get_amount_by_item_name(data: List[Dict], item_name: str) -> int:
    """
    Returns a value by key 'amount' from a dictionary whose value by key 'name' is equal to item_name
    """
    for item_dict in data:
        if item_dict['name'] == item_name:
            return item_dict['amount']


def get_total_price_by_item_name(data: List[Dict], item_name: str) -> float:
    """
    Returns a value by key 'total_price' from a dictionary whose value by key 'name' is equal to item_name
    """
    for item_dict in data:
        if item_dict['name'] == item_name:
            return item_dict['total_price']


def get_option_by_item_name(data: List[Dict], item_name: str) -> str:
    """
    Returns a value by key 'option' from a dictionary whose value by key 'name' is equal to item_name
    """
    for item_dict in data:
        if item_dict['name'] == item_name:
            return item_dict['option']


def get_pizza_names_with_option(data: List[Dict]) -> List[str]:
    """
    Returns a list of pizzas that have options
    """
    pizza_names = []
    for pizza_dict in data:
        if pizza_dict['option'] is not None:
            pizza_names.append(pizza_dict['name'])
    return pizza_names


def get_pizza_names_without_option(data: List[Dict]) -> List[str]:
    """
    Returns a list of pizzas that have no options
    """
    pizza_names = []
    for pizza_dict in data:
        if pizza_dict['option'] is None:
            pizza_names.append(pizza_dict['name'])
    return pizza_names


def get_edited_dict(start_dict: Dict) -> Dict:
    """
    Returns a dictionary with the changed type of quotes for keys
    """
    new_dict = {}
    for name in start_dict.keys():
        price = start_dict[name]
        new_dict[changes_quotes(name)] = price
    return new_dict


def get_total_cost_items_in_the_table(data: List[Dict]) -> float:
    """
    Returns the sum of values in dictionaries by key 'total_price'
    """
    total_cost = 0
    for item_dict in data:
        total_cost += item_dict['total_price']
    return total_cost


def get_next_day():
    """
    Returns the date of the next day
    """
    now = datetime.now()
    day = now.day
    month = now.month
    year = now.year
    today = date(year, month, day)
    next_day = today + timedelta(days=1)
    return next_day.day, next_day.month, next_day.year


def get_price(price: str) -> float:
    """
    Converts price in string format to float format
    """
    without_currency = price[:-1]
    replace_text = without_currency.replace(',', '.')
    edited_price = float(replace_text)
    return edited_price


def get_status_phone_number(phone_number: str) -> bool:
    """
    Checks if the phone number is Russian
    """
    pattern = r'regex(^((\+7|7|8)+([0-9]){10})$)'
    if re.match(pattern, phone_number) is not None:
        return True
    return False
