from .base_page import BasePage
from .locators import ProductPageLocators


class ProductPage(BasePage):
    def add_item_to_basket(self):
        item_link = self.browser.find_element(*ProductPageLocators.BUTTON)
        item_link.click()
