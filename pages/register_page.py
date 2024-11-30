import allure

from locators.register_page_locators import ANY_INPUT_LOCATOR, EMAIL_OR_NAME_LOCATOR, PASSWORD_LOCATOR, \
    REGISTER_BUTTON_LOCATOR
from pages.base_page import BasePage
from urls.urls import LOGIN_URL


class RegisterPage(BasePage):

    @allure.step('Регистрация пользователя')
    def register_user(self, random_email, random_password):
        self.open_register_page()
        self.wait_for_visibility(ANY_INPUT_LOCATOR)
        for input_element in self.find_all_elements(EMAIL_OR_NAME_LOCATOR):
            input_element.send_keys(random_email)
        self.find_element(PASSWORD_LOCATOR).send_keys(random_password)
        self.find_element(REGISTER_BUTTON_LOCATOR).click()
        self.wait_for_url_change(LOGIN_URL)
