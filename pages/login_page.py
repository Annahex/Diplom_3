import allure

from locators.login_page_locators import EMAIL_LOCATOR, PASSWORD_LOCATOR, LOGIN_BUTTON_LOCATOR, \
    FORGOT_PASSWORD_PAGE_LINK
from pages.base_page import BasePage
from urls.urls import FORGOT_PASSWORD_URL, BASE_URL


class LoginPage(BasePage):

    @allure.step('Проверка открытия страницы восстановления пароля')
    def check_forgot_password_page_opens(self):
        self.wait_to_be_clickable(FORGOT_PASSWORD_PAGE_LINK)
        self.find_element(FORGOT_PASSWORD_PAGE_LINK).click()
        self.wait_for_url_change(FORGOT_PASSWORD_URL)
        self.check_driver_url(FORGOT_PASSWORD_URL)

    @allure.step('Логин пользователя')
    def login(self, random_email, random_password):
        self.open_login_page()
        self.find_element(EMAIL_LOCATOR).send_keys(random_email)
        self.find_element(PASSWORD_LOCATOR).send_keys(random_password)
        self.find_element(LOGIN_BUTTON_LOCATOR).click()
        self.wait_for_url_change(BASE_URL)
