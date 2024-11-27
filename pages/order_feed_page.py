import data
from pages.base_page import BasePage
from locators.order_feed_page_locators import OrderFeedPageLocators
from locators.header_locators import HeaderLocators
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
import allure


class OrderFeedPage(BasePage):
    @allure.step('Открываем  страницу "Лента заказов"')
    def get_order_feed_page(self):
        if data.DRIVER_NAME == "chrome":
            self.get_main_page()
            self.click_to_element(HeaderLocators.ORDER_FEED_BUTTON_ON_THE_TOP)
        else:
            self.get_main_page()
            self.move_to_element_and_click_firefox(HeaderLocators.ORDER_FEED_BUTTON_ON_THE_TOP)

    @allure.step('получаем текст заколовка "Лента заказов"')
    def get_order_feed_page_header_text(self):
        return self.get_text_from_element(OrderFeedPageLocators.ORDER_FEED_PAGE_HEADER)

    @allure.step('Открываем  страницу "Конструктор"')
    def get_constructor_page(self):
        self.click_to_element(HeaderLocators.CONSTRUCTOR_BUTTON_ON_THE_TOP)

    @allure.step('Кликаем на заказ"')
    def click_to_order(self):
        if data.DRIVER_NAME == "chrome":
            self.click_to_element(OrderFeedPageLocators.ORDER_BOX)
        else:
            self.move_to_element_and_click_firefox(OrderFeedPageLocators.ORDER_BOX)

    @allure.step('получаем количество заказов за все время до заказа')
    def get_order_feed_page_and_get_all_time_counter_quantity_before_order(self):
        if data.DRIVER_NAME == "chrome":
            self.click_to_element(HeaderLocators.ORDER_FEED_BUTTON_ON_THE_TOP)
        else:
            self.move_to_element_and_click_firefox(HeaderLocators.ORDER_FEED_BUTTON_ON_THE_TOP)
        self.scroll_to_element(OrderFeedPageLocators.ALL_TIME_COUNTER)
        number = self.get_text_from_element(OrderFeedPageLocators.ALL_TIME_COUNTER)
        return int(number)

    @allure.step('получаем количество заказов за все время после заказа')
    def get_order_feed_page_and_get_all_time_counter_quantity_after_order(self, number):
        if data.DRIVER_NAME == "chrome":
            self.click_to_element(HeaderLocators.ORDER_FEED_BUTTON_ON_THE_TOP)
        else:
            self.move_to_element_and_click_firefox(HeaderLocators.ORDER_FEED_BUTTON_ON_THE_TOP)
        WebDriverWait(self.driver, 10).until(
            expected_conditions.text_to_be_present_in_element(OrderFeedPageLocators.IN_PROGRESS_LIST, number))
        self.scroll_to_element(OrderFeedPageLocators.ALL_TIME_COUNTER)
        number = self.get_text_from_element(OrderFeedPageLocators.ALL_TIME_COUNTER)
        return int(number)

    @allure.step('получаем количество заказов за сегодня до заказа')
    def get_order_feed_page_and_get_today_counter_quantity_before_order(self):
        if data.DRIVER_NAME == "chrome":
            self.click_to_element(HeaderLocators.ORDER_FEED_BUTTON_ON_THE_TOP)
        else:
            self.move_to_element_and_click_firefox(HeaderLocators.ORDER_FEED_BUTTON_ON_THE_TOP)
        self.scroll_to_element(OrderFeedPageLocators.TODAY_COUNTER)
        num = self.get_text_from_element(OrderFeedPageLocators.TODAY_COUNTER)
        return int(num)

    @allure.step('получаем количество заказов за сегодня после заказа')
    def get_order_feed_page_and_get_today_counter_quantity_after_order(self, number):
        if data.DRIVER_NAME == "chrome":
            self.click_to_element(HeaderLocators.ORDER_FEED_BUTTON_ON_THE_TOP)
        else:
            self.move_to_element_and_click_firefox(HeaderLocators.ORDER_FEED_BUTTON_ON_THE_TOP)
        WebDriverWait(self.driver, 10).until(
            expected_conditions.text_to_be_present_in_element(OrderFeedPageLocators.IN_PROGRESS_LIST, number))
        self.scroll_to_element(OrderFeedPageLocators.TODAY_COUNTER)
        num = self.get_text_from_element(OrderFeedPageLocators.TODAY_COUNTER)
        return int(num)

    @allure.step('получаем список заказов в работе')
    def get_order_feed_page_and_get_in_progress_list(self, number):
        if data.DRIVER_NAME == "chrome":
            self.click_to_element(HeaderLocators.ORDER_FEED_BUTTON_ON_THE_TOP)
        else:
            self.move_to_element_and_click_firefox(HeaderLocators.ORDER_FEED_BUTTON_ON_THE_TOP)
        self.get_text_from_element(OrderFeedPageLocators.IN_PROGRESS_LIST)
        WebDriverWait(self.driver, 10).until(expected_conditions.none_of(expected_conditions.text_to_be_present_in_element(OrderFeedPageLocators.IN_PROGRESS_LIST, 'Все текущие заказы готовы!')))
        WebDriverWait(self.driver, 10).until(expected_conditions.text_to_be_present_in_element(OrderFeedPageLocators.IN_PROGRESS_LIST, number))
        return self.get_text_from_element(OrderFeedPageLocators.IN_PROGRESS_LIST)

    @allure.step('получаем заголовок "Состав" из всплывающего окна с деталями об ингридиентах')
    def get_content_title_from_order_details_box(self):
        return self.get_text_from_element(OrderFeedPageLocators.CONTENT_TITLE_IN_ORDER_BOX)

    @allure.step('получаем последние 10 номеров заказов в ленте')
    def get_last_20_order_numbers(self):
        lst = self.find_elements(OrderFeedPageLocators.ORDER_NUMBERS)
        lst = list(lst)
        n = []
        for i in lst:
            n.append(i.text)
        return n[0:10]

