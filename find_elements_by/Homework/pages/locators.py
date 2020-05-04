from selenium.webdriver.common.by import By


class MainPageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, "#registration_link")


class LoginPageLocators:
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REGISTER_FORM = (By.CSS_SELECTOR, "#register_form")
    REGISTER_FORM_EMAIL = (By.CSS_SELECTOR, "#id_registration-email")
    REGISTER_FORM_PASSWORD_1 = (By.CSS_SELECTOR, "#id_registration-password1")
    REGISTER_FORM_PASSWORD_2 = (By.CSS_SELECTOR, "#id_registration-password2")
    REGISTER_FORM_BUTTON = (By.CSS_SELECTOR, "button[name = registration_submit]")


class ProductPageLocators:
    BUTTON_ADD_TO_BASKET = (By.CSS_SELECTOR, ".btn-add-to-basket")
    BOOK_TITLE = (By.CSS_SELECTOR, '.product_main h1')
    BOOK_PRICE = (By.CSS_SELECTOR, '.product_page .price_color')
    BASKET_BOOK_NAME = (By.CSS_SELECTOR, '#messages>div:nth-child(1) strong')
    BASKET_PRICE = (By.CSS_SELECTOR, '.alert-info .alertinner strong')
    SUCCESS_MESSAGE = (By.CSS_SELECTOR, '.alert-success:first-child')


class BasePageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    BASKET_LINK = (By.CSS_SELECTOR, ".basket-mini a")
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")


class BasketPageLocators:
    BASKET_SUMMARY = (By.CSS_SELECTOR, '.basket_summary')
    EMPTY_TEXT = (By.CSS_SELECTOR, '#content_inner p')
