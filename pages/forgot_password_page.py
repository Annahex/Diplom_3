import allure

from helpers.random_data import email
from locators.forgot_password_page_locators import *
from pages.base_page import BasePage


class ForgotPasswordPage(BasePage):

    @allure.step('Отправка запроса на восстановление пароля')
    def send_password_restore_request(self):
        self.wait_to_be_clickable(RESTORE_PASSWORD_BUTTON)
        self.find_element(RESTORE_EMAIL_INPUT).send_keys(email())
        self.find_element(RESTORE_PASSWORD_BUTTON).click()
        self.wait_for_visibility(RESTORE_PASSWORD_DIV_INPUT)

    @allure.step('Проверка отправки запроса на восстановление пароля')
    def check_password_restore_request_sent(self):
        self.wait_for_visibility(RESTORE_PASSWORD_DIV_INPUT)
        assert self.find_element(RESTORE_PASSWORD_DIV_INPUT).is_displayed()

    @allure.step('Нажатие на кнопку показать пароль')
    def click_on_focus_password_input_icon(self):
        self.wait_to_be_clickable(SHOW_HIDE_PASSWORD_BUTTON)
        self.find_element(SHOW_HIDE_PASSWORD_BUTTON).click()

    @allure.step('Проверка фокуса на поле пароля')
    def check_password_input_in_active_state(self):
        cls = self.find_element(RESTORE_PASSWORD_DIV_INPUT).get_attribute('class')
        assert "input_status_active" in cls
