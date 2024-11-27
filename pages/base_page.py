from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
import allure
from urls.urls import LOGIN_URL, FORGOT_PASSWORD_URL, BASE_URL


class BasePage:

    def __init__(self, driver):
        self.driver = driver

    @allure.step('Скролл до нужного элемента')
    def scroll_to(self, element):
        self.driver.execute_script("arguments[0].scrollIntoView();", element)

    @allure.step('Поиск элемента среди массива по индексу')
    def find_element_by_index(self, locator, index):
        return self.driver.find_elements(*locator)[index]

    @allure.step('Поиск элемента')
    def find_element(self, locator):
        return self.driver.find_element(*locator)

    @allure.step('Ожидание кликабельности элемента')
    def wait_to_be_clickable(self, locator):
        WebDriverWait(self.driver, 3).until(
            expected_conditions.element_to_be_clickable(tuple(locator)))

    @allure.step('Ожидание видимости элемента')
    def wait_for_visibility(self, locator):
        WebDriverWait(self.driver, 3).until(
            expected_conditions.visibility_of_element_located(tuple(locator)))

    @allure.step('Ожидание смены URL')
    def wait_for_url_change(self, url):
        WebDriverWait(self.driver, 3).until(
            expected_conditions.url_to_be(url))

    @allure.step('Открытие страницы логина')
    def open_login_page(self):
        self.driver.get(LOGIN_URL)
        self.wait_for_url_change(LOGIN_URL)

    @allure.step('Открытие страницы восстановления пароля')
    def open_forgot_password_page(self):
        self.driver.get(FORGOT_PASSWORD_URL)
        self.wait_for_url_change(FORGOT_PASSWORD_URL)

    @allure.step('Открытие страницы конструктора')
    def open_main_page(self):
        self.driver.get(BASE_URL)
        self.wait_for_url_change(BASE_URL)


