from pages.base_page import BasePage
from locators.main_page_locators import (MainPageLocators)
import allure


class MainPage(BasePage):
    @allure.step('Открываем главную страницу и нажимаем на кнопку личный кабинет')
    def open_main_page_and_get_login_page(self):
        self.get_main_page()
        self.click_to_element(MainPageLocators.PROFILE_BUTTON_LOCATOR)

