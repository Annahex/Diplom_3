from selenium.webdriver.common.by import By

RESTORE_PASSWORD_BUTTON = [By.XPATH, ".//button[text()='Восстановить']"]
RESTORE_EMAIL_INPUT = [By.XPATH, ".//input[@name='name']"]
RESTORE_PASSWORD_DIV_INPUT = [By.XPATH, ".//input[@name='Введите новый пароль']/parent::div"]
SHOW_HIDE_PASSWORD_BUTTON = [By.XPATH,
                             ".//input[@name='Введите новый пароль']/following-sibling::div[starts-with(@class,'input__icon')]"]
