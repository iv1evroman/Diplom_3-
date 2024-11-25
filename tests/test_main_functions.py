import time

import data
from pages.main_page import MainPage
from pages.login_page import LoginPage
from pages.order_feed_page import OrderFeedPage
from locators.main_page_locators import MainPageLocators
import allure


class TestMainFunctions:
    @allure.title('Тест на переход по клику на «Лента заказов»')
    def test_transition_to_order_feed_page(self, driver):
        order_page = OrderFeedPage(driver)
        order_page.get_order_feed_page()
        assert order_page.get_order_feed_page_header_text() == 'Лента заказов'

    @allure.title('Тест на переход по клику на «Конструктор»')
    def test_transition_to_constructor_page(self, driver):
        order_page = OrderFeedPage(driver)
        order_page.get_order_feed_page()
        order_page.get_constructor_page()
        assert driver.current_url == data.MAIN_PAGE_URL

    @allure.title('Тест на то, что если кликнуть на ингредиент, появится всплывающее окно с деталями')
    def test_click_to_ingredient_and_get_details(self, driver):
        main_page = MainPage(driver)
        assert main_page.open_main_page_click_to_spicy_sauce_and_get_text_from_details_card() == 'Детали ингредиента'

    @allure.title('Тест на то, что всплывающее окно закрывается кликом по крестику')
    def test_click_to_cross_and_close_ingredient_details(self, driver):
        main_page = MainPage(driver)
        main_page.open_main_page_click_to_spicy_sauce_and_click_to_close_details_card()
        status = main_page.find_element_with_wait(MainPageLocators.INGREDIENT_DETAILS_BOX)
        assert status.get_attribute('class') == 'Modal_modal__P3_V5'

    @allure.title('Тест на то, что при добавлении ингредиента в заказ, увеличивается каунтер данного ингредиента')
    def test_add_ingredient_to_order_and_verify_that_ingredient_counter_increases(self, driver):
        main_page = MainPage(driver)
        assert main_page.open_main_page_and_add_ingredient_to_order() == '1'

    @allure.title('Тест на то, что залогиненный пользователь может оформить заказ')
    def test_login_and_create_order(self, driver):
        main_page = MainPage(driver)
        login_page = LoginPage(driver)
        main_page.open_main_page_and_get_login_page()
        login_page.login_test_account(data.EMAIL_FOR_ORDERS)
        main_page.add_ingredient_and_create_order()
        assert main_page.get_text_from_element(MainPageLocators.ORDER_IS_PREPARING) == 'Ваш заказ начали готовить'