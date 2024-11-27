from selenium.webdriver.common.by import By
import allure
from urls.urls import FEED_URL
from pages.base_page import BasePage


class FeedPage(BasePage):

    feed_lnk = (By.XPATH, ".//a[@href='/feed']")

    @allure.step('Открытие страницы ленты заказа')
    def click_to_open_feed_page(self):
        self.wait_to_be_clickable(self.feed_lnk)
        self.find_element(self.feed_lnk).click()
        self.wait_for_url_change(FEED_URL)

    @allure.step('Проверка открытия страницы ленты заказов')
    def check_feed_page_opens(self):
        assert self.driver.current_url == FEED_URL



