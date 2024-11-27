
from pages.constructor_page import ConstructorPage
import allure


class TestConstructorPage:

    @allure.title('Проверка открытия страницы конструктора')
    def test_open_profile_from_header(self, driver):
        feed_page = ConstructorPage(driver)
        feed_page.open_login_page()
        feed_page.click_to_open_constructor_page()
        feed_page.check_constructor_page_opens()


