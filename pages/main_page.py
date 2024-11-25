import time

import data
from pages.base_page import BasePage
from locators.main_page_locators import (MainPageLocators)
import allure


class MainPage(BasePage):
    @allure.step('Открываем главную страницу и нажимаем на кнопку личный кабинет')
    def open_main_page_and_get_login_page(self):
        self.get_main_page()
        self.click_to_element(MainPageLocators.PROFILE_BUTTON_LOCATOR)

    @allure.step('Открываем главную страницу, нажимаем на острый соус и получаем текст с деталями об ингредиенте')
    def open_main_page_click_to_spicy_sauce_and_get_text_from_details_card(self):
        self.get_main_page()
        self.click_to_element(MainPageLocators.SPICY_SAUCE_BUTTON)
        return self.get_text_from_element(MainPageLocators.DETAILS_CARD_HEADER)

    @allure.step('Открываем главную страницу, нажимаем на острый соус, и закрываем карточку с деталями об ингредиентах')
    def open_main_page_click_to_spicy_sauce_and_click_to_close_details_card(self):
        self.get_main_page()
        self.click_to_element(MainPageLocators.SPICY_SAUCE_BUTTON)
        self.click_to_element(MainPageLocators.CLOSE_DETAILS_CARD_BUTTON)

    @allure.step('Открываем главную страницу и добавляем ингредиент в заказ  и получаем цифру на каунтере ингредиента')
    def open_main_page_and_add_ingredient_to_order(self):
        if data.DRIVER_NAME == "chrome":
            self.get_main_page()
            self.def_drag_and_drop_element_chrome(MainPageLocators.SPICY_SAUCE_BUTTON, MainPageLocators.ORDER_BASKET)
            return self.get_text_from_element(MainPageLocators.SPICY_SAUCE_COUNTER)
        else:
            self.get_main_page()
            self.drag_and_drop_element_firefox(MainPageLocators.SPICY_SAUCE_BUTTON, MainPageLocators.ORDER_BASKET)
            return self.get_text_from_element(MainPageLocators.SPICY_SAUCE_COUNTER)

    @allure.step('Добавляем ингредиент в заказ и нажимаем кнопку "Оформить заказ"')
    def add_ingredient_and_create_order(self):
        if data.DRIVER_NAME == "chrome":
            self.def_drag_and_drop_element_chrome(MainPageLocators.SPICY_SAUCE_BUTTON, MainPageLocators.ORDER_BASKET)
            self.click_to_element(MainPageLocators.CREATE_ORDER_BUTTON)
        else:
            self.drag_and_drop_element_firefox(MainPageLocators.SPICY_SAUCE_BUTTON, MainPageLocators.ORDER_BASKET)
            self.click_to_element(MainPageLocators.CREATE_ORDER_BUTTON)