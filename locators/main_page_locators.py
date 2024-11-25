from selenium.webdriver.common.by import By


class MainPageLocators:
    PROFILE_BUTTON_LOCATOR = By.XPATH, './/a[contains(@href, "account")]' # Кнопка личный кабинет
    FLUORESCENT_BUN_BUTTON = (
    By.XPATH, './/img[contains(@alt, "Флюоресцентная булка R2-D3")]')  # Кнопка выбора флюоресцентной булки
    SPICY_SAUCE_BUTTON = (By.XPATH, './/img[contains(@alt, "Соус Spicy-X")]')  # Кнопка выбора острого соуса
    DETAILS_CARD_HEADER = (By.XPATH, './/h2[contains(text(),"Детали ингредиента")]')  # Заголовок карточки деталей
    # ингредиента
    CLOSE_DETAILS_CARD_BUTTON = \
        (By.XPATH, './/button[@class="Modal_modal__close_modified__3V5XS Modal_modal__close__TnseK"]')  # Крестик
    # закрытия карточки деталей об ингредиенте
    INGREDIENT_DETAILS_BOX = \
        (By.XPATH, './/div[@class="Modal_modal__container__Wo2l_"]/parent::section')  # Родительский элемент section
    # окна деталей об ингредиентах
    ORDER_BASKET = (By.XPATH, './/ul[@class="BurgerConstructor_basket__list__l9dp_"]')  # Корзина заказа на
    # главной странице
    SPICY_SAUCE_COUNTER = (By.XPATH, './/a[contains(@href, "/ingredient/61c0c5a71d1f82001bdaaa72")]/div/p')  # Каунтер
    # острого соуса
    CREATE_ORDER_BUTTON = (By.XPATH, './/button[contains(text(),"Оформить заказ")]')  # Кнопка оформить заказ
    ORDER_IS_PREPARING = By.XPATH, './/p[contains(text(),"Ваш заказ начали готовить")]'