from pages.order_feed_page import OrderFeedPage
from pages.main_page import MainPage
from pages.login_page import LoginPage
from pages.profile_page import ProfilePage
import allure


class TestOrderFeedPage:
    @allure.title('Тест на то, что если кликнуть на заказ, откроется всплывающее окно с деталями')
    def test_open_order_details_window(self, driver):
        order_feed_page = OrderFeedPage(driver)
        order_feed_page.get_order_feed_page()
        order_feed_page.click_to_order()
        assert order_feed_page.get_content_title_from_order_details_box() == 'Cостав'

    @allure.title('Тест на то, что заказы пользователя из раздела «История заказов» отображаются на'
                  ' странице «Лента заказов»')
    def test_order_number_from_history_section_displays_in_order_feed(self, driver):
        main_page = MainPage(driver)
        login_page = LoginPage(driver)
        profile_page = ProfilePage(driver)
        order_feed_page = OrderFeedPage(driver)
        main_page.open_main_page_and_get_login_page()
        login_page.login_test_account_for_orders()
        main_page.add_ingredient_and_create_order()
        main_page.wait_for_new_order_number()
        main_page.close_order_details_card()
        profile_page.get_orders_history_page()
        number = profile_page.get_last_order_number()
        order_feed_page.get_order_feed_page()
        assert number in order_feed_page.get_last_20_order_numbers()

    @allure.title('Тест на то, что при создании нового заказа счётчик Выполнено за всё время увеличивается')
    def test_create_order_and_all_time_counter_increases(self, driver):
        order_feed_page = OrderFeedPage(driver)
        main_page = MainPage(driver)
        login_page = LoginPage(driver)
        main_page.get_main_page()
        before_order_quantity = order_feed_page.get_order_feed_page_and_get_all_time_counter_quantity_before_order()
        main_page.open_main_page_and_get_login_page()
        login_page.login_test_account_for_orders()
        main_page.add_ingredient_and_create_order()
        main_page.wait_for_new_order_number()
        number = main_page.get_new_order_number()
        main_page.close_order_details_card()
        after_order_quantity = order_feed_page.get_order_feed_page_and_get_all_time_counter_quantity_after_order(number)
        assert after_order_quantity > before_order_quantity

    @allure.title('Тест на то, что при создании нового заказа счётчик Выполнено за сегодня увеличивается')
    def test_create_order_and_today_counter_increases(self, driver):
        order_feed_page = OrderFeedPage(driver)
        main_page = MainPage(driver)
        login_page = LoginPage(driver)
        main_page.get_main_page()
        before_order_quantity = order_feed_page.get_order_feed_page_and_get_today_counter_quantity_before_order()
        main_page.open_main_page_and_get_login_page()
        login_page.login_test_account_for_orders()
        main_page.add_ingredient_and_create_order()
        main_page.wait_for_new_order_number()
        number = main_page.get_new_order_number()
        main_page.close_order_details_card()
        after_order_quantity = order_feed_page.get_order_feed_page_and_get_today_counter_quantity_after_order(number)
        assert after_order_quantity > before_order_quantity

    @allure.title('Тест на то, что после оформления заказа его номер появляется в разделе В работе.')
    def test_after_creation_of_order_its_number_displays_in_progress_section(self,  driver):
        order_feed_page = OrderFeedPage(driver)
        main_page = MainPage(driver)
        login_page = LoginPage(driver)
        main_page.open_main_page_and_get_login_page()
        login_page.login_test_account_for_orders()
        main_page.add_ingredient_and_create_order()
        main_page.wait_for_new_order_number()
        number = main_page.get_new_order_number()
        main_page.close_order_details_card()
        assert number in order_feed_page.get_order_feed_page_and_get_in_progress_list(number)
