import allure

from locators.feed_page_locators import *
from pages.base_page import BasePage
from urls.urls import FEED_URL


class FeedPage(BasePage):

    @allure.step('Открытие страницы ленты заказа')
    def click_to_open_feed_page(self):
        self.wait_to_be_clickable(FEED_LINK)
        self.find_element(FEED_LINK).click()
        self.wait_for_url_change(FEED_URL)

    @allure.step('Проверка открытия страницы ленты заказов')
    def check_feed_page_opens(self):
        self.check_driver_url(FEED_URL)

    @allure.step('Открытие информации о заказе')
    def click_to_open_order_info(self):
        self.wait_to_be_clickable(HISTORY_ITEM)
        self.find_element_by_index(HISTORY_ITEM, 0).click()

    @allure.step('Проверка открытия информации о заказе')
    def check_open_order_info(self):
        self.wait_for_visibility(ITEM_INFO_HEADER)
        assert self.find_element(ITEM_INFO_HEADER).is_displayed()

    @allure.step('Проверка наличия своего заказа в общем списке')
    def check_order_id_in_all_orders(self, order_id):
        self.wait_for_visibility(HISTORY_ID)
        for item in self.find_all_elements(HISTORY_ID):
            if item.text == order_id:
                break
        else:
            assert False
        assert True

    @allure.step('Получение счетчиков заказов за все время')
    def get_order_total_counter(self):
        self.wait_for_visibility(ORDER_TOTAL_COUNTER)
        counters = self.find_all_elements(ORDER_TOTAL_COUNTER)
        return int(counters[0].text)

    @allure.step('Получение счетчиков заказов за все сегодня')
    def get_order_today_counter(self):
        self.wait_for_visibility(ORDER_TODAY_COUNTER)
        counters = self.find_all_elements(ORDER_TODAY_COUNTER)
        return int(counters[0].text)

    @allure.step('Ожидание инкремента счетчика за все время')
    def wait_for_total_counter_increment(self, value):
        self.wait_for_text_appear(ORDER_TOTAL_COUNTER, value)

    @allure.step('Ожидание инкремента счетчика за все сегодня')
    def wait_for_today_counter_increment(self, value):
        self.wait_for_text_appear(ORDER_TODAY_COUNTER, value)

    @allure.step('Ожидание появления id заказа')
    def wait_for_order_appears(self, order_id):
        self.wait_for_text_appear(NOT_READY_ORDERS, order_id)

    @allure.step('Получение счетчиков заказов')
    def get_not_ready_order_ids(self):
        self.wait_for_visibility(NOT_READY_ORDERS)
        elements = self.find_all_elements(NOT_READY_ORDERS)
        return list(map(lambda e: e.text, elements))
