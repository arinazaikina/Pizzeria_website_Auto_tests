class PizzaPageLocators:
    PIZZA_NAME = "//div/h1[@class='product_title entry-title']"
    PIZZA_PRICE = "//div[@class='summary entry-summary']//bdi"
    SELECT = "//select[@id='board_pack']"
    REGULAR = "//select[@id='board_pack']/option[contains(text(), 'Обычный')]"
    CHEESE = "//select[@id='board_pack']/option[contains(text(), 'Сырный')]"
    SAUSAGE = "//select[@id='board_pack']/option[contains(text(), 'Колбасный')]"
    ADD_TO_CART = "//button[@name='add-to-cart']"
    ALERT = "//div[@role='alert']"
