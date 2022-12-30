class MainPageLocators:
    ACTIVE_PIZZA = "//aside[@id='accesspress_store_product-5']/ul/div/div/li[contains(@class, 'slick-active')]/a"
    PIZZA_LINK = "//h2[contains(text(), 'Пицца')]/parent::div/following-sibling::ul/div/div/li/a"

    @classmethod
    def get_image_locator_by_pizza_name(cls, pizza_name: str):
        """
        Returns XPATH of pizza image by pizza name on maim page
        """
        return f"//aside[@id='accesspress_store_product-5']/ul/div/div/" \
               f"li[contains(@class, 'slick-active')]/div/a[@title='{pizza_name}']"

    @classmethod
    def get_price_locator(cls, pizza_name: str):
        """
        Returns XPATH of pizza price by pizza name on maim page
        """
        return f"//li[contains(@class, 'slick-active')]/a[contains(@title, '{pizza_name}')]" \
               f"/span/span[contains(@class, 'amount')]"

    @classmethod
    def get_direction_button(cls, direction: str):
        """
        Returns the locator of the scroll button of the slider in the specified direction on maim page
        """
        return f"//a[@class='slick-{direction}']"

    @classmethod
    def get_cart_locator_by_pizza_name(cls, pizza_name: str):
        """
        Returns XPATH of TO CART button by pizza name on maim page
        """
        return f"//li[contains(@class, 'slick-active')]//a[@title='{pizza_name}']/parent::div/a[2]"

    @classmethod
    def get_more_button_locator_by_pizza_name(cls, pizza_name):
        """
        Returns XPATH of MORE button by pizza name on maim page
        """
        return f"//li[contains(@class, 'slick-active')]//a[@title='{pizza_name}']/parent::div/a[3]"
