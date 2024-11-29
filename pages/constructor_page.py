import allure

from locators.constructor_page_locators import *
from pages.base_page import BasePage
from urls.urls import BASE_URL


class ConstructorPage(BasePage):

    @allure.step('Открытие страницы конструктора')
    def click_to_open_constructor_page(self):
        self.wait_to_be_clickable(CONSTRUCTOR_LINK)
        self.find_element(CONSTRUCTOR_LINK).click()
        self.wait_for_url_change(BASE_URL)

    @allure.step('Проверка открытия страницы конструктора')
    def check_constructor_page_opens(self):
        assert self.driver.current_url == BASE_URL

    @allure.step('Открытие попапа ингредиента')
    def click_to_open_ingredient_popup(self):
        self.wait_to_be_clickable(INGREDIENT_LINK)
        self.find_element_by_index(INGREDIENT_LINK, 0).click()
        self.wait_for_visibility(CLOSE_INGREDIENT_MODAL)

    @allure.step('Проверка открытия попапа ингредиента')
    def check_ingredient_popup_open(self):
        assert self.find_element(CLOSE_INGREDIENT_MODAL).is_displayed()

    @allure.step('Закрытие попапа ингредиента')
    def click_to_close_ingredient_popup(self):
        self.wait_to_be_clickable(CLOSE_INGREDIENT_MODAL)
        self.find_element(CLOSE_INGREDIENT_MODAL).click()
        self.wait_for_invisibility(CLOSE_INGREDIENT_MODAL)

    @allure.step('Проверка закрытия попапа ингредиента')
    def check_ingredient_popup_close(self):
        assert self.find_element(CLOSE_INGREDIENT_MODAL).is_displayed() is False

    @allure.step('Выбор ингредиента')
    def move_ingredient_to_basket(self):
        self.wait_to_be_clickable(INGREDIENT_LINK)
        ingredient = self.find_element_by_index(INGREDIENT_LINK, 0)
        basket = self.find_element(BASKET_ELEMENT)
        self.drag_and_drop(ingredient, basket)

    @allure.step('Проерка выбора ингредиента')
    def check_ingredient_counter_increases(self):
        counter = self.find_element_by_index(INGREDIENT_COUNTER, 0)
        assert int(counter.text) > 0

    @allure.step('Оформить заказ')
    def create_order(self):
        self.wait_to_be_clickable(CREATE_ORDER_BUTTON)
        self.find_element(CREATE_ORDER_BUTTON).click()

    @allure.step('Проерка оформления заказа')
    def check_create_order(self):
        self.wait_for_visibility(ORDER_ID_HEADER)
        order_id = self.find_element(ORDER_ID_HEADER)
        assert int(order_id.text) > 0
