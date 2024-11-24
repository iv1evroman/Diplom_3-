from selenium.webdriver.common.by import By


class PasswordRecoveryPageLocators:
    RECOVERY_BUTTON = By.XPATH, './/button[contains(text(),"Восстановить")]'  # кнопка Восстановить на странице
    # восстановления пароля
    EMAIL_INPUT_FIELD_ON_RECOVERY_PAGE = (By.XPATH, '//label[ text()="Email" ]/parent::div/input')  # Поле ввода email
    # на странице восстановления пароля
    SAVE_BUTTON_ON_RECOVERY_PAGE = (By.XPATH, './/button[contains(text(),"Сохранить")]')  # Кнопка Сохранить под формой
    # ввода нового пароля
    PASSWORD_INPUT_FIELD_ON_RECOVERY_PAGE = (By.XPATH, '//label[ text()="Пароль" ]/parent::div/input')  # Поле пароль
    # на форме ввода нового пароля
    SHOW_AND_HIDE_BUTTON = By.XPATH, "//svg:svg[@fill='#F2F2F3']"  # Кнопка показать/скрыть пароль