import data
from pages.base_page import BasePage
from locators.profile_page_locators import ProfilePageLocators
import allure
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class ProfilePage(BasePage):
    @allure.step('Нажимаем на кнопку история заказов')
    def get_orders_history_page(self):
        if data.DRIVER_NAME == "chrome":
            WebDriverWait(self.driver, 10).until(
                expected_conditions.visibility_of_element_located(ProfilePageLocators.PROFILE_BUTTON_LOCATOR))
            self.click_to_element(ProfilePageLocators.PROFILE_BUTTON_LOCATOR)
            self.click_to_element(ProfilePageLocators.PROFILE_BUTTON_LOCATOR)
            self.click_to_element(ProfilePageLocators.HISTORY_BUTTON_ON_PERSONAL_ACCOUNT_PAGE)
        else:
            WebDriverWait(self.driver, 10).until(
                expected_conditions.visibility_of_element_located(ProfilePageLocators.PROFILE_BUTTON_LOCATOR))
            self.move_to_element_and_click_firefox(ProfilePageLocators.PROFILE_BUTTON_LOCATOR)
            self.move_to_element_and_click_firefox(ProfilePageLocators.PROFILE_BUTTON_LOCATOR)
            self.move_to_element_and_click_firefox(ProfilePageLocators.HISTORY_BUTTON_ON_PERSONAL_ACCOUNT_PAGE)

    @allure.step('Нажимаем на кнопку выход на странице профиля')
    def push_exit_button(self):
        WebDriverWait(self.driver, 10).until(expected_conditions.visibility_of_element_located(ProfilePageLocators.PROFILE_BUTTON_LOCATOR))
        if data.DRIVER_NAME == "chrome":
            self.click_to_element(ProfilePageLocators.PROFILE_BUTTON_LOCATOR)
            self.click_to_element(ProfilePageLocators.PROFILE_BUTTON_LOCATOR)
            self.click_to_element(ProfilePageLocators.EXIT_BUTTON_ON_PROFILE_PAGE)
        else:
            self.move_to_element_and_click_firefox(ProfilePageLocators.PROFILE_BUTTON_LOCATOR)
            self.move_to_element_and_click_firefox(ProfilePageLocators.PROFILE_BUTTON_LOCATOR)
            self.move_to_element_and_click_firefox(ProfilePageLocators.EXIT_BUTTON_ON_PROFILE_PAGE)

    @allure.step('получаем номер тестового заказа')
    def get_test_order_number(self):
        return self.get_text_from_element(ProfilePageLocators.TEST_ORDER)

    @allure.step('получаем номер последнего заказа')
    def get_last_order_number(self):
        return self.get_text_from_element(ProfilePageLocators.LAST_CREATED_ORDER_ON_HISTORY_SECTION)
