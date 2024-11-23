from selenium.webdriver.common.by import By


class LoginPageLocators:
    PASSWORD_RECOVERY_BUTTON_ON_LOGIN_PAGE = By.XPATH, './/a[contains(@href, "forgot-password")]' # Кнопка Восстановить
    # пароль на странице входа
    EMAIL_INPUT_FIELD_LOGIN_FORM = By.XPATH, './/input[@name="name"]'  # Поле email на форме входа
    PASSWORD_INPUT_FIELD_LOGIN_FORM = (By.XPATH, './/input[@name="Пароль"]')  # Поле пароль на форме входа
    LOGIN_BUTTON_ON_LOGIN_FORM = (By.XPATH, './/button[contains(text(),"Войти")]')  # Кнопка Войти на форме входа