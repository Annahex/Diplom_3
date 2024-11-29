from selenium.webdriver.common.by import By

EMAIL_LOCATOR = [By.XPATH, ".//main//form//input[@name='name']"]
PASSWORD_LOCATOR = [By.XPATH, ".//main//form//input[@name='Пароль']"]
LOGIN_BUTTON_LOCATOR = [By.XPATH, ".//button[text()='Войти']"]
FORGOT_PASSWORD_PAGE_LINK = [By.XPATH, ".//a[@href='/forgot-password']"]
