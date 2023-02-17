import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from pageObjects.login_page import LoginPage

@pytest.fixture()
def browser() -> webdriver:
    driver = webdriver.Chrome(service=Service('./chromedriver'))
    driver.maximize_window()
    return driver

@pytest.fixture()
def login_as_standard_user(browser) -> None:
        browser.get("https://www.saucedemo.com/")
        login_page = LoginPage(browser)
        login_page.set_user_name("standard_user")
        login_page.set_password("secret_sauce")
        login_page.click_login_button()
