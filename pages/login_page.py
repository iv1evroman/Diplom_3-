import data
from pages.base_page import BasePage
from locators.login_page_locators import LoginPageLocators
import allure


class LoginPage(BasePage):
    @allure.step('Получаем текст с кнопки восстановить пароль')
    def get_text_from_recovery_page_button(self):
        return self.get_text_from_element(LoginPageLocators.PASSWORD_RECOVERY_BUTTON_ON_LOGIN_PAGE)

    @allure.step('входим в личный кабинет тестового аккаунта')
    def login_test_account(self):
        self.add_text_to_element(LoginPageLocators.EMAIL_INPUT_FIELD_LOGIN_FORM, data.TEST_ACCOUNT_EMAIL)
        self.add_text_to_element(LoginPageLocators.PASSWORD_INPUT_FIELD_LOGIN_FORM, data.TEST_ACCOUNT_PASSWORD)
        if data.DRIVER_NAME == "chrome":
            self.click_to_element(LoginPageLocators.LOGIN_BUTTON_ON_LOGIN_FORM)
        else:
            self.move_to_element_and_click_firefox(LoginPageLocators.LOGIN_BUTTON_ON_LOGIN_FORM)

    @allure.step('входим в личный кабинет тестового аккаунта для заказов')
    def login_test_account_for_orders(self):
        self.add_text_to_element(LoginPageLocators.EMAIL_INPUT_FIELD_LOGIN_FORM, data.EMAIL_FOR_ORDERS)
        self.add_text_to_element(LoginPageLocators.PASSWORD_INPUT_FIELD_LOGIN_FORM, data.TEST_ACCOUNT_PASSWORD)
        if data.DRIVER_NAME == "chrome":
            self.click_to_element(LoginPageLocators.LOGIN_BUTTON_ON_LOGIN_FORM)
        else:
            self.move_to_element_and_click_firefox(LoginPageLocators.LOGIN_BUTTON_ON_LOGIN_FORM)

    @allure.step('Открываем страницу восстановления пароля')
    def get_password_recovery_page(self):
        if data.DRIVER_NAME == "chrome":
            self.scroll_to_element(LoginPageLocators.PASSWORD_RECOVERY_BUTTON_ON_LOGIN_PAGE)
            self.click_to_element(LoginPageLocators.PASSWORD_RECOVERY_BUTTON_ON_LOGIN_PAGE)
        else:
            self.scroll_to_element(LoginPageLocators.PASSWORD_RECOVERY_BUTTON_ON_LOGIN_PAGE)
            self.move_to_element_and_click_firefox(LoginPageLocators.PASSWORD_RECOVERY_BUTTON_ON_LOGIN_PAGE)