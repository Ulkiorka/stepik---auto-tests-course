from selenium.webdriver.common.by import By


class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#registration_link")

class LoginPageLocators():
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REGISTER_FORM = (By.CSS_SELECTOR, "#register_form")

class ProductPageLocators():
    BUTTON = (By.CSS_SELECTOR, ".btn-add-to-basket")
    MESSAGE_AFTER_ADD_ITEM = (By.CSS_SELECTOR, '.alert-success:first-child .alertinner strong')
    PRODUCT_PRICE = (By.CSS_SELECTOR, '.product_page .price_color')
    BASCET_PRICE = (By.CSS_SELECTOR, 'div.alert div p strong')
