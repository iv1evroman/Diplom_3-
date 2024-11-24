import data
from pages.base_page import BasePage
from locators.password_recovery_page_locators import PasswordRecoveryPageLocators
import allure


class PasswordRecoveryPage(BasePage):
    @allure.step('Получаем текст с кнопки "Восстановить" страницы восстановления пароля')
    def get_text_from_recovery_button_on_password_recovery_page(self):
        return self.get_text_from_element(PasswordRecoveryPageLocators.RECOVERY_BUTTON)

    @allure.step('Вводим тестовый email на странице восстановления пароля и кликаем по кнопке "Восстановить')
    def input_test_email_for_password_recovery_and_click_on_recovery_button(self):
        self.add_text_to_element(PasswordRecoveryPageLocators.EMAIL_INPUT_FIELD_ON_RECOVERY_PAGE,
                                 data.TEST_ACCOUNT_EMAIL)
        self.click_to_element(PasswordRecoveryPageLocators.RECOVERY_BUTTON)

    @allure.step('Получаем текст с кнопки "Сохранить" под формой ввода нового пароля')
    def get_text_from_code_input(self):
        return self.get_text_from_element(PasswordRecoveryPageLocators.SAVE_BUTTON_ON_RECOVERY_PAGE)

    @allure.step('кликаем на кнопку показать/скрыть пароль в поле ввода нового пароля')
    def click_show_and_hide_button_in_password_field(self):
        self.click_to_element(PasswordRecoveryPageLocators.SHOW_AND_HIDE_BUTTON)

    @allure.step('Получаем значение атрибута type поля ввода нового пароля в форме восстановления пароля')
    def get_type_attribute_of_new_password_field(self):
        elm = self.find_element_with_wait(PasswordRecoveryPageLocators.PASSWORD_INPUT_FIELD_ON_RECOVERY_PAGE)
        return elm.get_attribute('type')
