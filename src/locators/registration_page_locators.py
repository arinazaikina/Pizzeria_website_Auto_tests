class RegistrationLocators:
    USERNAME = "//label[@for='reg_username']/following-sibling::input"
    EMAIL = "//input[@type='email']"
    PASSWORD = "//input[@type='password']"
    BUTTON = "//button[@value='Зарегистрироваться']"
    SUCCESSFUL_REGISTRATION = "//div[contains(text(), 'Регистрация завершена')]"
    USERNAME_IN_NAVIGATION = "//span[@class='user-name']"
    ERROR_MESSAGE = "//ul[@class='woocommerce-error']/li"
