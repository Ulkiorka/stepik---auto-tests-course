from .base_page import BasePage
from .locators import ProductPageLocators


class ProductPage(BasePage):
    def add_item_to_basket(self):
        """Метод добавления товара в корзину"""
        item_link = self.browser.find_element(*ProductPageLocators.BUTTON_ADD_TO_BASKET)
        item_link.click()

    def check_add_item_to_basket(self):
        """Проверка: товар добавлен в корзину"""
        self.message_items_should_be_add_to_basket()
        self.should_be_same_prices()

    def message_items_should_be_add_to_basket(self):
        """Проверка: название товара в сообщении совпадает с добавленным товаром"""
        book_title = self.browser.find_element(*ProductPageLocators.BOOK_TITLE).text
        message_after_add = self.browser.find_element(*ProductPageLocators.BASKET_BOOK_NAME).text
        assert book_title == message_after_add, f"book title does not match name in message: '{book_title}' != '{message_after_add}'"

    def should_be_same_prices(self):
        """Проверка: стоимость корзины равна цене товара"""
        product_price = self.browser.find_element(*ProductPageLocators.BOOK_PRICE).text
        price_in_basket = self.browser.find_element(*ProductPageLocators.BASKET_PRICE).text
        print(product_price, price_in_basket)
        assert product_price == price_in_basket, f"{product_price} not equal {price_in_basket}"

    def should_not_be_success_message(self):
        """Проверка, что элемент не появился на странице"""
        assert self.is_not_element_present(*ProductPageLocators.SUCCESS_MESSAGE), \
            "Success message is presented, but should not be"

    def message_should_be_disappeared(self):
        """Проверка, что элемент исчез спустя заданное время"""
        assert self.is_disappeared(*ProductPageLocators.SUCCESS_MESSAGE), \
                'Success message is not disappeared, but should be'