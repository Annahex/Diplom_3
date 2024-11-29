from selenium.webdriver.common.by import By

FEED_LINK = (By.XPATH, ".//a[@href='/feed']")
HISTORY_ITEM = (By.XPATH, ".//li[starts-with(@class, 'OrderHistory_listItem')]")
HISTORY_ID = (By.XPATH, ".//p[starts-with(@class, 'text text_type_digits-default')]")
ITEM_INFO_HEADER = (By.XPATH, ".//p[text()='Cостав']")
ORDER_COUNTER = (By.XPATH, ".//p[starts-with(@class, 'OrderFeed_number__')]")
NOT_READY_ORDERS = (By.XPATH,
                    ".//ul[starts-with(@class, 'OrderFeed_orderListReady__')]/li[starts-with(@class, 'text text_type_digits-default')]")
