from pages.main_page import MainPage
from pages.login_page import LoginPage
from pages.profile_page import ProfilePage
from locators.profile_page_locators import ProfilePageLocators
import allure


class TestProfilePage:
    @allure.title('Тест на переход по клику на «Личный кабинет»')
    def test_open_profile_page(self, driver):
        main_page = MainPage(driver)
        login_page = LoginPage(driver)
        main_page.open_main_page_and_get_login_page()
        assert login_page.get_text_from_recovery_page_button() == 'Восстановить пароль'

    @allure.title('Тест на переход в раздел «История заказов»')
    def test_open_orders_history_page(self, driver):
        main_page = MainPage(driver)
        login_page = LoginPage(driver)
        profile_page = ProfilePage(driver)
        main_page.open_main_page_and_get_login_page()
        login_page.login_test_account()
        profile_page.get_orders_history_page()
        assert '#0152756' in profile_page.get_text_from_element(ProfilePageLocators.TEST_ORDER)

    @allure.title('Тест на выход из аккаунта')
    def test_exit_profile(self, driver):
        main_page = MainPage(driver)
        login_page = LoginPage(driver)
        profile_page = ProfilePage(driver)
        main_page.open_main_page_and_get_login_page()
        login_page.login_test_account()
        profile_page.push_exit_button()
        assert login_page.get_text_from_recovery_page_button() == 'Восстановить пароль'
