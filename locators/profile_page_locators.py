from selenium.webdriver.common.by import By


class ProfilePageLocators:
    PROFILE_BUTTON_LOCATOR = By.XPATH, './/a[contains(@href, "account")]'  # Кнопка личный кабинет
    HISTORY_BUTTON_ON_PERSONAL_ACCOUNT_PAGE = By.XPATH, './/a[contains(text(),"История заказов")]'  # Кнопка
    # Профиль на странице Личный кабинет
    TEST_ORDER = (
        By.XPATH, ".//*[contains(text(), '#0152756') and starts-with(@class, 'text text_type_digits-default')]")
    # тестовый заказ на странице истории заказов
    EXIT_BUTTON_ON_PROFILE_PAGE = (By.XPATH, './/button[contains(text(),"Выход")]')  # Кнопка выход
    # на странице Личного кабинета
    LAST_CREATED_ORDER_ON_HISTORY_SECTION = (By.XPATH, '/html/body/div/div/main/div/div/div/ul/li[1]/a/div[1]/p[1]')  #
    # Последний созданный заказ в разделе история заказов
