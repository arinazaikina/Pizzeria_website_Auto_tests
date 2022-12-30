class MenuPageLocators:
    LEFT_BUTTON = "//div[@class='price_slider_wrapper']/div/span[1]"
    RIGHT_BUTTON = "//div[@class='price_slider_wrapper']/div/span[2]"
    SUBMIT_FILTER = "//div[@class='price_slider_amount']/button[@type='submit']"
    ITEMS_NAME = "//ul[@class='products columns-4']/li/div[@class='collection_desc clearfix']/a/h3"
    TOP_PRICE = "//div[@class='price_label']/span[2]"

    @classmethod
    def get_price_item_locator_by_name(cls, item_name: str):
        """
        Returns XPATH of price by position name on menu page
        """
        return f"//h3[contains(text(), '{item_name}')]/parent::a/following-sibling::div/span/span/bdi"

    @classmethod
    def get_to_cart_locator_by_name(cls, item_name: str):
        """
        Returns XPATH of TO CART button by pizza name on menu page
        """
        return f"//h3[contains(text(), '{item_name}')]/parent::a/following-sibling::div/a"

    @classmethod
    def get_more_locator_by_name(cls, item_name: str):
        """
        Returns XPATH of MORE button by pizza name on menu page
        """
        return f"//h3[contains(text(), '{item_name}')]/parent::a/following-sibling::div/a[@title='Подробнее']"
