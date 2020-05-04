from .base_page import BasePage
from .locators import BasketPageLocators


class BasketPage(BasePage):
    def should_be_no_items(self):
        """Проверка что в корзине нет товаров"""
        assert self.is_not_element_present(*BasketPageLocators.BASKET_SUMMARY), "basket is not empty"

    def should_be_empty_message(self):
        empty_text = self.browser.find_element(*BasketPageLocators.EMPTY_TEXT).text
        assert "Ваша корзина пуста" in empty_text , "empty basket text is absent"