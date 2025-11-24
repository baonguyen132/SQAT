from ssl import Options
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options

import pytest

@pytest.fixture
def driver():
    chrome_options = Options()
    chrome_options.add_argument("--start-maximized")

    # Selenium Manager tự tải driver
    driver = webdriver.Chrome(options=chrome_options)

    yield driver
    driver.quit()

@pytest.fixture
def driverLogin():
    chrome_options = Options()
    chrome_options.add_argument("--start-maximized")
    driver = webdriver.Chrome(options=chrome_options)
    driver.get("https://www.saucedemo.com/")
    # Login trước khi test giỏ hàng
    driver.find_element(By.ID, "user-name").send_keys("standard_user")
    driver.find_element(By.ID, "password").send_keys("secret_sauce")
    driver.find_element(By.ID, "login-button").click()
    yield driver
    driver.quit()