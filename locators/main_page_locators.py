from selenium.webdriver.common.by import By


class MainPageLocators:
    PROFILE_BUTTON_LOCATOR = By.XPATH, './/a[contains(@href, "account")]' # Кнопка личный кабинет
