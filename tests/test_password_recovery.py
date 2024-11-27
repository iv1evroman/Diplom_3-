import time

from pages.main_page import MainPage
from pages.login_page import LoginPage
from pages.password_recovery_page import PasswordRecoveryPage
import allure


class TestProfilePage:
    @allure.title('Тест на переход на страницу восстановления пароля по кнопке «Восстановить пароль»')
    def test_get_password_recovery_page_by_clicking_recovery_password_button(self, driver):
        main_page = MainPage(driver)
        login_page = LoginPage(driver)
        password_recovery_page = PasswordRecoveryPage(driver)
        main_page.open_main_page_and_get_login_page()
        login_page.get_password_recovery_page()
        assert password_recovery_page.get_text_from_recovery_button_on_password_recovery_page() == "Восстановить"

    @allure.title('Тест на ввод почты и клик по кнопке «Восстановить»')
    def test_input_email_and_click_recovery_button_on_password_recovery_page(self, driver):
        main_page = MainPage(driver)
        login_page = LoginPage(driver)
        password_recovery_page = PasswordRecoveryPage(driver)
        main_page.open_main_page_and_get_login_page()
        login_page.get_password_recovery_page()
        password_recovery_page.input_test_email_for_password_recovery_and_click_on_recovery_button()
        assert password_recovery_page.get_text_from_code_input() == 'Сохранить'

    @allure.title('Тест на клик по кнопке показать/скрыть пароль делает поле активным — подсвечивает его.')
    def test_click_show_and_hide_button_on_password_recovery_page(self, driver):
        main_page = MainPage(driver)
        login_page = LoginPage(driver)
        password_recovery_page = PasswordRecoveryPage(driver)
        main_page.open_main_page_and_get_login_page()
        login_page.get_password_recovery_page()
        password_recovery_page.input_test_email_for_password_recovery_and_click_on_recovery_button()
        password_recovery_page.click_show_and_hide_button_in_password_field()
        assert password_recovery_page.get_type_attribute_of_new_password_field() == 'text'
