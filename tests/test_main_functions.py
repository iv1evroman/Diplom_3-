import time

from pages.main_page import MainPage
from pages.order_feed_page import OrderFeedPage
from pages.order_feed_page import OrderFeedPageLocators
import allure


class TestMainFunctions:
    @allure.title('Тест на переход по клику на «Лента заказов»')
    def test_transition_to_order_feed_page(self, driver):
        order_page = OrderFeedPage(driver)
        order_page.get_order_feed_page()
        time.sleep(3)
        assert order_page.get_order_feed_page_header_text() == 'Лента заказов'
