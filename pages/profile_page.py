import allure

from locators.profile_page_locators import *
from pages.base_page import BasePage
from urls.urls import PROFILE_URL, ORDER_HISTORY_URL, LOGIN_URL


class ProfilePage(BasePage):

    @allure.step('Открытие страницы профиля')
    def open_profile_page(self):
        self.wait_to_be_clickable(PROFILE_PAGE_LINK)
        self.find_element(PROFILE_PAGE_LINK).click()
        self.wait_for_url_change(PROFILE_URL)

    @allure.step('Проверка открытия страницы профиля')
    def check_profile_page_opens(self):
        assert self.driver.current_url == PROFILE_URL

    @allure.step('Открытие страницы истории заказов')
    def open_order_history_page(self):
        self.wait_to_be_clickable(ORDER_HISTORY_LINK)
        self.find_element(ORDER_HISTORY_LINK).click()
        self.wait_for_url_change(ORDER_HISTORY_URL)

    @allure.step('Получение последнего id заказа')
    def get_last_order_id(self):
        self.wait_for_visibility(ORDER_ID)
        return self.find_element_by_index(ORDER_ID, 0).text

    @allure.step('Проверка открытия страницы истории заказов')
    def check_order_history_page_opens(self):
        assert self.driver.current_url == ORDER_HISTORY_URL

    @allure.step('Выход из ЛК')
    def logout(self):
        self.wait_to_be_clickable(LOGOUT_BUTTON)
        self.find_element(LOGOUT_BUTTON).click()
        self.wait_for_url_change(LOGIN_URL)

    @allure.step('Проверка выхода из ЛК')
    def check_logout(self):
        assert self.driver.current_url == LOGIN_URL
