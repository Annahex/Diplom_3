from selenium.webdriver.common.by import By
import allure
from urls.urls import BASE_URL
from pages.base_page import BasePage


class ConstructorPage(BasePage):

    constructor_link = (By.XPATH, ".//p[text()='Конструктор']//parent::a[@href='/']")

    @allure.step('Открытие страницы конструктора')
    def click_to_open_constructor_page(self):
        self.wait_to_be_clickable(self.constructor_link)
        self.find_element(self.constructor_link).click()
        self.wait_for_url_change(BASE_URL)

    @allure.step('Проверка открытия страницы конструктора')
    def check_constructor_page_opens(self):
        assert self.driver.current_url == BASE_URL



