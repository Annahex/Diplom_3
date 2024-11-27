
from pages.feed_page import FeedPage
import allure


class TestFeedPage:

    @allure.title('Проверка открытия страницы лента заказов')
    def test_open_profile_from_header(self, driver):
        feed_page = FeedPage(driver)
        feed_page.open_main_page()
        feed_page.click_to_open_feed_page()
        feed_page.check_feed_page_opens()


