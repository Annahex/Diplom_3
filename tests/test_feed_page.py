import time

from pages.feed_page import FeedPage
from pages.profile_page import ProfilePage
from pages.constructor_page import ConstructorPage
import allure


class TestFeedPage:

    @allure.title('Проверка открытия страницы лента заказов')
    def test_open_profile_from_header(self, driver):
        feed_page = FeedPage(driver)
        feed_page.open_main_page()
        feed_page.click_to_open_feed_page()
        feed_page.check_feed_page_opens()

    @allure.title('Проверка открытия информации о заказе')
    def test_open_profile_from_header(self, driver):
        feed_page = FeedPage(driver)
        feed_page.open_main_page()
        feed_page.click_to_open_feed_page()
        feed_page.click_to_open_order_info()
        feed_page.check_open_order_info()

    @allure.title('Проверка наличия заказа пользователя в общей истории')
    def test_open_profile_from_header(self, driver_logged_in):
        constructor_page = ConstructorPage(driver_logged_in)
        constructor_page.open_main_page()
        constructor_page.move_ingredient_to_basket()
        constructor_page.create_order()
        constructor_page.open_main_page()
        profile_page = ProfilePage(driver_logged_in)
        profile_page.open_profile_page()
        profile_page.open_order_history_page()
        order_id = profile_page.get_last_order_id()
        feed_page = FeedPage(driver_logged_in)
        feed_page.click_to_open_feed_page()
        feed_page.check_order_id_in_all_orders(order_id)
