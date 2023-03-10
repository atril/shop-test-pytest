import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from pageObjects.login_page import LoginPage
from utils import config

@pytest.fixture()
def browser() -> webdriver:
    driver = webdriver.Chrome(service=Service('./chromedriver'))
    driver.maximize_window()
    yield driver
    driver.quit()

@pytest.fixture()
def login_as_standard_user(browser) -> None:
        browser.get(config.url)
        login_page = LoginPage(browser)
        login_page.set_user_name(config.standard_user_name)
        login_page.set_password(config.standard_user_password)
        login_page.click_login_button()
