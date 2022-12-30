class CartPageLocators:
    ITEM_LIST = "//tbody//td[@class='product-name']/a"
    ALERT = "//div[@role='alert']"
    UPDATE_CART = "//button[@name='update_cart']"
    TOTAL_COST_IN_SUMMARY = "//table[@class='shop_table shop_table_responsive']/tbody/tr/td/span/bdi"
    SUM_IN_SUMMARY = "//tr[@class='order-total']/td/strong/span/bdi"
    GO_TO_THE_PAYMENT = "//a[@class='checkout-button button alt wc-forward']"

    @classmethod
    def get_delete_locator_by_item_name(cls, item_name: str):
        """
        Returns XPATH of the delete button by position name on cart page
        """
        return f"//a[contains(text(), '{item_name}')]/parent::td/preceding-sibling::td[@class='product-remove']/a"

    @classmethod
    def get_price_locator_by_item_name(cls, item_name: str):
        """
        Returns XPATH of price by position name on cart page
        """
        return f"//a[contains(text(), '{item_name}')]/parent::td[@class='product-name']/following-sibling::td[" \
               f"@class='product-price'] "

    @classmethod
    def get_amount_locator_by_item_name(cls, item_name: str):
        """
        Returns XPATH of amount by position name on cart page
        """
        return f"//a[contains(text(), '{item_name}')]/parent::td[@class='product-name']/" \
               f"following::td[@class='product-quantity']/div/label[contains(text(), '{item_name}')]/" \
               f"following-sibling::input"

    @classmethod
    def get_total_price_locator_by_item_name(cls, item_name: str):
        """
        Returns XPATH of total price by position name on cart page
        """
        return f"//a[contains(text(), '{item_name}')]/parent::td[@class='product-name']/following-sibling::td[" \
               f"@class='product-subtotal'] "

    @classmethod
    def get_option_locator_by_item_name(cls, item_name: str):
        """
        Returns XPATH of option by position name on cart page
        """
        return f"//a[contains(text(), '{item_name}')]/parent::td[@class='product-name']/child::dl/dd/p"
