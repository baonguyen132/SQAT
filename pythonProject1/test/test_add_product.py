# -------------------------
# Thêm 1 sản phẩm vào giỏ
# -------------------------
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC  # BẮT BUỘC

def test_add_single_product(driverLogin):
    wait = WebDriverWait(driverLogin, 10)

    # Thêm sản phẩm đầu tiên
    add_button = wait.until(EC.element_to_be_clickable((By.ID, "add-to-cart-sauce-labs-backpack")))
    add_button.click()

    # Kiểm tra số lượng giỏ hàng
    cart_badge = wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "shopping_cart_badge")))
    assert cart_badge.text == "1"

    # Vào trang giỏ hàng
    driverLogin.find_element(By.CLASS_NAME, "shopping_cart_link").click()

    # Kiểm tra sản phẩm trong giỏ
    cart_item = wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "inventory_item_name")))
    assert cart_item.text == "Sauce Labs Backpack"


# -------------------------
# Thêm nhiều sản phẩm
# -------------------------
def test_add_multiple_products(driverLogin):
    wait = WebDriverWait(driverLogin, 10)

    # Thêm sản phẩm thứ 1
    driverLogin.find_element(By.ID, "add-to-cart-sauce-labs-backpack").click()
    # Thêm sản phẩm thứ 2
    driverLogin.find_element(By.ID, "add-to-cart-sauce-labs-bike-light").click()

    # Kiểm tra số lượng giỏ hàng
    cart_badge = wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "shopping_cart_badge")))
    assert cart_badge.text == "2"

    # Vào trang giỏ hàng
    driverLogin.find_element(By.CLASS_NAME, "shopping_cart_link").click()

    # Kiểm tra sản phẩm 1
    cart_items = driverLogin.find_elements(By.CLASS_NAME, "inventory_item_name")
    product_names = [item.text for item in cart_items]

    assert "Sauce Labs Backpack" in product_names
    assert "Sauce Labs Bike Light" in product_names