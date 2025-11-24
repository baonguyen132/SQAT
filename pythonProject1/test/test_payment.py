import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# -------------------------
# Thanh toán hợp lệ
# -------------------------
def test_checkout_success(driverLogin):
    wait = WebDriverWait(driverLogin, 10)

    # Thêm sản phẩm
    driverLogin.find_element(By.ID, "add-to-cart-sauce-labs-backpack").click()
    driverLogin.find_element(By.ID, "add-to-cart-sauce-labs-bike-light").click()

    # Vào giỏ hàng và Checkout
    driverLogin.find_element(By.CLASS_NAME, "shopping_cart_link").click()
    driverLogin.find_element(By.ID, "checkout").click()

    # Điền thông tin hợp lệ
    driverLogin.find_element(By.ID, "first-name").send_keys("Nguyen")
    driverLogin.find_element(By.ID, "last-name").send_keys("Bao")
    driverLogin.find_element(By.ID, "postal-code").send_keys("700000")
    driverLogin.find_element(By.ID, "continue").click()

    # Chờ sản phẩm Overview load
    items_elements = wait.until(
        EC.visibility_of_all_elements_located((By.CLASS_NAME, "inventory_item_name"))
    )
    items = [e.text for e in items_elements]
    assert "Sauce Labs Backpack" in items
    assert "Sauce Labs Bike Light" in items

    # Kiểm tra tổng tiền
    subtotal = driverLogin.find_element(By.CLASS_NAME, "summary_subtotal_label").text
    assert "Item total" in subtotal

    # Nhấn Finish
    driverLogin.find_element(By.ID, "finish").click()

    # Chờ thông báo đặt hàng thành công (dùng XPath để chắc chắn)
    complete_text = wait.until(
        EC.presence_of_element_located(
            (By.XPATH, "//h2[contains(text(),'Thank you for your order')]")
        )
    ).text
    assert complete_text.strip() == "Thank you for your order!"

@pytest.mark.parametrize(
    "first,last,zip,expected_error",
    [
        ("", "Bao", "700000", "Error: First Name is required"),
        ("Nguyen", "", "700000", "Error: Last Name is required"),
        ("Nguyen", "Bao", "", "Error: Postal Code is required"),
        ("", "", "", "Error: First Name is required")  # tất cả bỏ trống
    ]
)
def test_checkout_missing_info(driverLogin, first, last, zip, expected_error):
    wait = WebDriverWait(driverLogin, 10)

    # Thêm sản phẩm
    driverLogin.find_element(By.ID, "add-to-cart-sauce-labs-backpack").click()
    driverLogin.find_element(By.CLASS_NAME, "shopping_cart_link").click()
    driverLogin.find_element(By.ID, "checkout").click()

    # Điền thông tin cá nhân
    driverLogin.find_element(By.ID, "first-name").send_keys(first)
    driverLogin.find_element(By.ID, "last-name").send_keys(last)
    driverLogin.find_element(By.ID, "postal-code").send_keys(zip)
    driverLogin.find_element(By.ID, "continue").click()

    # Kiểm tra thông báo lỗi
    error_text = wait.until(
        EC.visibility_of_element_located((By.CSS_SELECTOR, "h3[data-test='error']"))
    ).text
    assert error_text == expected_error