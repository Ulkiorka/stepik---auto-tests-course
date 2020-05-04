from .base_page import BasePage
from .locators import LoginPageLocators
import time

class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        # реализуйте проверку на корректный url адрес
        assert 'login' in self.browser.current_url, "this is nt login-page"

    def should_be_login_form(self):
        # реализуйте проверку, что есть форма логина
        assert self.is_element_present(*LoginPageLocators.LOGIN_FORM), "Login form is absent"

    def should_be_register_form(self):
        # реализуйте проверку, что есть форма регистрации на странице
        assert self.is_element_present(*LoginPageLocators.REGISTER_FORM), "Register form is absent"

    def register_new_user(self, email, password):
        """Метод: регистрирует нового пользователя"""
        email_field = self.browser.find_element(*LoginPageLocators.REGISTER_FORM_EMAIL)
        email_field.send_keys(email)
        password_field1 = self.browser.find_element(*LoginPageLocators.REGISTER_FORM_PASSWORD_1)
        password_field1.send_keys(password)
        password_field2 = self.browser.find_element(*LoginPageLocators.REGISTER_FORM_PASSWORD_2)
        password_field2.send_keys(password)
        button_submit = self.browser.find_element(*LoginPageLocators.REGISTER_FORM_BUTTON)
        button_submit.click()

