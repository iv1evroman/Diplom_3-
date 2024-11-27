from selenium.webdriver.common.by import By


class OrderFeedPageLocators:
    ORDER_FEED_PAGE_HEADER = (By.XPATH, './/h1[contains(text(),"Лента заказов")]')
    ORDER_BOX = By.XPATH, './/li[@class="OrderHistory_listItem__2x95r mb-6"]'
    CONTENT_TITLE_IN_ORDER_BOX = By.XPATH, './/p[contains(text(),"Cостав")]'
    ALL_TIME_COUNTER = (By.XPATH, '/html/body/div/div/main/div/div/div/div[2]/p[2]')
    TODAY_COUNTER = (By.XPATH, '/html/body/div/div/main/div/div/div/div[3]/p[2]')
    IN_PROGRESS_LIST = (By.XPATH, './/ul[@class="OrderFeed_orderListReady__1YFem OrderFeed_orderList__cBvyi"]/li')
    ORDER_NUMBERS = (By.XPATH, '/html/body/div/div/main/div/div/ul/li[position()<20]/a/div[1]/p[1]')  # Номера заказов в ленте
