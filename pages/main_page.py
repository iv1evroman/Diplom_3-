import data
from pages.base_page import BasePage
from locators.main_page_locators import (MainPageLocators)
import allure
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class MainPage(BasePage):
    @allure.step('Открываем главную страницу и нажимаем на кнопку личный кабинет')
    def open_main_page_and_get_login_page(self):
        if data.DRIVER_NAME == "chrome":
            self.get_main_page()
            self.click_to_element(MainPageLocators.PROFILE_BUTTON_LOCATOR)
        else:
            self.get_main_page()
            self.move_to_element_and_click_firefox(MainPageLocators.PROFILE_BUTTON_LOCATOR)

    @allure.step('Открываем главную страницу, нажимаем на острый соус и получаем текст с деталями об ингредиенте')
    def open_main_page_click_to_spicy_sauce_and_get_text_from_details_card(self):
        if data.DRIVER_NAME == "chrome":
            self.get_main_page()
            self.scroll_to_element(MainPageLocators.SPICY_SAUCE_BUTTON)
            self.click_to_element(MainPageLocators.SPICY_SAUCE_BUTTON)
        else:
            self.get_main_page()
            self.scroll_to_element(MainPageLocators.SPICY_SAUCE_BUTTON)
            self.move_to_element_and_click_firefox(MainPageLocators.SPICY_SAUCE_BUTTON)
        return self.get_text_from_element(MainPageLocators.DETAILS_CARD_HEADER)

    @allure.step('Открываем главную страницу, нажимаем на острый соус, и закрываем карточку с деталями об ингредиентах')
    def open_main_page_click_to_spicy_sauce_and_click_to_close_details_card(self):
        if data.DRIVER_NAME == "chrome":
            self.get_main_page()
            self.scroll_to_element(MainPageLocators.SPICY_SAUCE_BUTTON)
            self.click_to_element(MainPageLocators.SPICY_SAUCE_BUTTON)
            self.click_to_element(MainPageLocators.CLOSE_DETAILS_CARD_BUTTON)
        else:
            self.get_main_page()
            self.scroll_to_element(MainPageLocators.SPICY_SAUCE_BUTTON)
            self.move_to_element_and_click_firefox(MainPageLocators.SPICY_SAUCE_BUTTON)
            self.move_to_element_and_click_firefox(MainPageLocators.CLOSE_DETAILS_CARD_BUTTON)

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
            self.def_drag_and_drop_element_chrome(MainPageLocators.FLUORESCENT_BUN_BUTTON,
                                                  MainPageLocators.ORDER_BASKET)
            self.click_to_element(MainPageLocators.CREATE_ORDER_BUTTON)
        else:
            self.drag_and_drop_element_firefox(MainPageLocators.FLUORESCENT_BUN_BUTTON, MainPageLocators.ORDER_BASKET)
            self.move_to_element_and_click_firefox(MainPageLocators.CREATE_ORDER_BUTTON)

    @allure.step('ждем когда появится номер нового заказа')
    def wait_for_new_order_number(self):
        self.get_text_from_element(MainPageLocators.ORDER_NUMBER_ON_NEW_ORDER_CARD)
        WebDriverWait(self.driver, 10).until(expected_conditions.none_of(expected_conditions.text_to_be_present_in_element(MainPageLocators.ORDER_NUMBER_ON_NEW_ORDER_CARD, '9999')))

    @allure.step('закрываем карточку с деталями об ингредиентах')
    def close_order_details_card(self):
        if data.DRIVER_NAME == "chrome":
            self.click_to_element(MainPageLocators.CLOSE_DETAILS_CARD_BUTTON)
        else:
            self.move_to_element_and_click_firefox(MainPageLocators.CLOSE_DETAILS_CARD_BUTTON)

    @allure.step('получаем номер созданного заказа')
    def get_new_order_number(self):
        return self.get_text_from_element(MainPageLocators.ORDER_NUMBER_ON_NEW_ORDER_CARD)

    @allure.step('находим родительский элемент section окна деталей об ингредиентах')
    def get_parent_element_of_ingredient_details_box(self):
        return self.find_element_with_wait(MainPageLocators.INGREDIENT_DETAILS_BOX)

    @allure.step('Получаем текст "Ваш заказ начали готовить"')
    def get_order_is_ready_text(self):
        if self.get_text_from_element(MainPageLocators.ORDER_IS_PREPARING) == 'Ваш заказ начали готовить':
            return True
        else:
            return False
