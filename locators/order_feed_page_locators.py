from selenium.webdriver.common.by import By


class OrderFeedPageLocators:
    ORDER_FEED_PAGE_HEADER = (By.XPATH, './/h1[contains(text(),"Лента заказов")]')
    