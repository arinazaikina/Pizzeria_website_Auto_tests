class OrderingLocators:
    NAME = "//input[@id='billing_first_name']"
    SURNAME = "//input[@id='billing_last_name']"
    COUNTRY = "//span[@id='select2-billing_country-container']"
    COUNTRY_INPUT = "//input[@class='select2-search__field']"
    ADDRESS = "//input[@id='billing_address_1']"
    CITY = "//input[@id='billing_city']"
    STATE = "//input[@id='billing_state']"
    POSTCODE = "//input[@id='billing_postcode']"
    PHONE = "//input[@id='billing_phone']"
    EMAIL = "//input[@id='billing_email']"
    DATE = "//input[@id='order_date']"
    PAYMENT_ON_DELIVERY = "//input[@id='payment_method_cod']"
    TERMS_AND_CONDITIONS = "//input[@type='checkbox']"
    BUTTON = "//button[@id='place_order']"
    MESSAGE_ABOUT_DELIVERY = "//div[@class='payment_box payment_method_cod']/p"
    ITEMS_LIST = "//td[@class='product-name']"
    TOTAL_COST = "//tr[@class='cart-subtotal']/td/span/bdi"
    SUM = "//tr[@class='order-total']/td/strong/span/bdi"
    ITEMS_LIST_FOR_DETAIL_ORDER = "//td[@class='woocommerce-table__product-name product-name']/a"
    SUBTOTAL = "//th[contains(text(), 'Subtotal:')]/parent::tr/td/span"
    PAYMENT_METHOD = "//th[contains(text(), 'Payment method:')]/following-sibling::td"
    TOTAL = "//th[contains(text(), 'Total:')]/parent::tr/td/span"
    ADDRESS_TO_SEND_A_CHECK = "//address"
    PHONE_IN_ORDER_DETAILS = "//p[@class='woocommerce-customer-details--phone']"
    EMAIL_IN_ORDER_DETAILS = "//p[@class='woocommerce-customer-details--email']"
    SHOW_COUPON = "//a[@class='showcoupon']"
    INPUT_COUPON = "//input[@id='coupon_code']"
    APPLY_COUPON = "//button[@name='apply_coupon']"
    ALERT = "//div[@role='alert']"
    ERROR_ALERT = "//ul[@class='woocommerce-error']/li"
    DISCOUNT = "//tr[@class='cart-discount coupon-givemehalyava']/td/span"
    DISCOUNT_ORDER_DETAILS = "//th[contains(text(), 'Discount')]/parent::tr/td/span"

    @classmethod
    def get_total_price_item_locator_by_name(cls, item_name: str):
        """
        Returns XPATH of total price by position name on ordering page
        """
        return f"//*[contains(text(), '{item_name}')]/following-sibling::td/span/bdi"

    @classmethod
    def get_total_cost_item_locator_by_name_for_detail_order(cls, item_name: str):
        """
        Returns XPATH of total cost by position name on details order page
        """
        return f"//*[contains(text(), '{item_name}')]/parent::td/following-sibling::td/span/bdi"

    @classmethod
    def get_amount_item_locator_by_name_for_detail_order(cls, item_name: str):
        """
        Returns XPATH of amount by position name on details order page
        """
        return f"//a[contains(text(), '{item_name}')]/following-sibling::strong"
