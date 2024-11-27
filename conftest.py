from selenium import webdriver
import pytest


@pytest.fixture(params=["firefox", "chrome"])
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
