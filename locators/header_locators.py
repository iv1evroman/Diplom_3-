from selenium.webdriver.common.by import By


class HeaderLocators:
    ORDER_FEED_BUTTON_ON_THE_TOP = (By.XPATH, './/p[contains(text(),"Лента Заказов")]')  # Кнопка лента заказв в шапке
    CONSTRUCTOR_BUTTON_ON_THE_TOP = (By.XPATH, './/p[contains(text(),"Конструктор")]')  # Кнопка конструктор на шапке
    # сайта
