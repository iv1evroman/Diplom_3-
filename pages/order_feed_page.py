from pages.base_page import BasePage
from locators.order_feed_page_locators import OrderFeedPageLocators
from locators.header_locators import HeaderLocators
import allure


class OrderFeedPage(BasePage):
    @allure.step('Открываем  страницу "Лента заказов"')
    def get_order_feed_page(self):
        self.get_main_page()
        self.click_to_element(HeaderLocators.ORDER_FEED_BUTTON_ON_THE_TOP)

    @allure.step('получаем текст заколовка "Лента заказов"')
    def get_order_feed_page_header_text(self):
        return self.get_text_from_element(OrderFeedPageLocators.ORDER_FEED_PAGE_HEADER)

    @allure.step('Открываем  страницу "Конструктор"')
    def get_constructor_page(self):
        self.click_to_element(HeaderLocators.CONSTRUCTOR_BUTTON_ON_THE_TOP)