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
        self.click_to_element(LoginPageLocators.LOGIN_BUTTON_ON_LOGIN_FORM)


