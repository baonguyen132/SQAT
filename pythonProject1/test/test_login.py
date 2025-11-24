import time

from selenium.webdriver.common.by import By


# -----------------------------
# 1. Test đăng nhập thành công
# -----------------------------
def test_login_success(driver):
    driver.get("https://www.saucedemo.com/")

    driver.find_element(By.ID, "user-name").send_keys("standard_user")
    driver.find_element(By.ID, "password").send_keys("secret_sauce")
    driver.find_element(By.ID, "login-button").click()

    time.sleep(1)

    assert driver.current_url == "https://www.saucedemo.com/inventory.html"

def test_login_wrong_password(driver):
    driver.get("https://www.saucedemo.com/")

    driver.find_element(By.ID, "user-name").send_keys("standard_user")
    driver.find_element(By.ID, "password").send_keys("sssa")
    driver.find_element(By.ID, "login-button").click()

    time.sleep(1)

    error = driver.find_element(By.ID, "data-test").text
    assert error.inclue("Epic sadface: Username and password do not match any user in this service")
    assert driver.current_url == "https://www.saucedemo.com/"

def test_login_wrong_username(driver):
    driver.get("https://www.saucedemo.com/")

    driver.find_element(By.ID, "user-name").send_keys("ssaas")
    driver.find_element(By.ID, "password").send_keys("secret_sauce")
    driver.find_element(By.ID, "login-button").click()

    time.sleep(1)

    error = driver.find_element(By.ID, "error").text
    assert error == "Sai username"
    assert driver.current_url == "https://www.saucedemo.com/"


def test_login_wrong_both(driver):
    driver.get("https://www.saucedemo.com/")

    driver.find_element(By.ID, "user-name").send_keys("ssaas")
    driver.find_element(By.ID, "password").send_keys("sssa")
    driver.find_element(By.ID, "login-button").click()

    time.sleep(1)

    error = driver.find_element(By.ID, "error").text
    assert error == "Thông tin đăng nhập không đúng"
    assert driver.current_url == "https://www.saucedemo.com/"

def test_login_empty(driver):
    driver.get("https://www.saucedemo.com/")

    driver.find_element(By.ID, "user-name").send_keys("")
    driver.find_element(By.ID, "password").send_keys("")
    driver.find_element(By.ID, "login-button").click()

    time.sleep(1)

    error = driver.find_element(By.ID, "error").text
    assert error == "Không được để trống thông tin đăng nhập"
    assert driver.current_url == "https://www.saucedemo.com/"
