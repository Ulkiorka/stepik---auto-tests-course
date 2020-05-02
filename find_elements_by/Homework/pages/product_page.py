from .base_page import BasePage
from .locators import ProductPageLocators


class ProductPage(BasePage):
    def add_item_to_basket(self):
        item_link = self.browser.find_element(*ProductPageLocators.BUTTON)
        item_link.click()

    def check_add_item_to_basket(self):
        self.should_be_message()
        self.should_be_right_price()

    def should_be_message(self):
        assert self.is_element_present(*ProductPageLocators.MESSAGE_AFTER_ADD_ITEM), "item was not added"

    def should_be_right_price(self):
        product_price = self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE).text
        bascet_price  = self.browser.find_element(*ProductPageLocators.BASCET_PRICE).text
        print(product_price, bascet_price)
        assert product_price == bascet_price, f"{product_price} not equal {bascet_price}"