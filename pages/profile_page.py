import time

import data
from pages.base_page import BasePage
from locators.profile_page_locators import ProfilePageLocators
import allure


class ProfilePage(BasePage):
    @allure.step('Нажимаем на кнопку история заказов')
    def get_orders_history_page(self):
        self.click_to_element(ProfilePageLocators.PROFILE_BUTTON_LOCATOR)
        self.click_to_element(ProfilePageLocators.HISTORY_BUTTON_ON_PERSONAL_ACCOUNT_PAGE)

    @allure.step('Нажимаем на кнопку выход на странице профиля')
    def push_exit_button(self):
        self.click_to_element(ProfilePageLocators.PROFILE_BUTTON_LOCATOR)
        self.click_to_element(ProfilePageLocators.EXIT_BUTTON_ON_PROFILE_PAGE)