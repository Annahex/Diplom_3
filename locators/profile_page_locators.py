from selenium.webdriver.common.by import By

PROFILE_PAGE_LINK = [By.XPATH, ".//a[@href='/account']"]
ORDER_HISTORY_LINK = [By.XPATH, ".//a[@href='/account/order-history']"]
LOGOUT_BUTTON = [By.XPATH, ".//button[text()='Выход']"]
ORDER_ID = [By.XPATH, ".//p[starts-with(@class, 'text text_type_digits-default')]"]
