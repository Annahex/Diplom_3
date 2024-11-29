import pytest
from selenium import webdriver

from helpers.random_data import email, password
from pages.login_page import LoginPage
from pages.register_page import RegisterPage
from urls.urls import REGISTER_URL


@pytest.fixture()
def random_email():
    return email()


@pytest.fixture()
def random_password():
    return password()


@pytest.fixture(params=["chrome"])
def driver(request):
    browser = request.param
    if browser == "chrome":
        driver = webdriver.Chrome()
    elif browser == "firefox":
        driver = webdriver.Firefox()
    else:
        raise ValueError()
    yield driver
    driver.quit()


@pytest.fixture()
def driver_registered(driver, random_email, random_password):
    driver.get(REGISTER_URL)
    page = RegisterPage(driver)
    page.register_user(random_email, random_password)
    return driver


@pytest.fixture()
def driver_logged_in(driver_registered, random_email, random_password):
    page = LoginPage(driver_registered)
    page.login(random_email, random_password)
    return driver_registered
