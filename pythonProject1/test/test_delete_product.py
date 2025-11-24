from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
# -------------------------
# Xóa sản phẩm từ giỏ hàng
# -------------------------
def test_remove_product_from_cart(driverLogin):
    wait = WebDriverWait(driverLogin, 10)

    # Thêm sản phẩm vào giỏ
    driverLogin.find_element(By.ID, "add-to-cart-sauce-labs-backpack").click()

    # Vào trang giỏ hàng
    driverLogin.find_element(By.CLASS_NAME, "shopping_cart_link").click()

    # Xóa sản phẩm trong giỏ
    remove_button = wait.until(
        EC.element_to_be_clickable((By.ID, "remove-sauce-labs-backpack"))
    )
    remove_button.click()

    # Kiểm tra giỏ hàng trống
    cart_items = driverLogin.find_elements(By.CLASS_NAME, "cart_item")
    assert len(cart_items) == 0

# -------------------------
# Xóa sản phẩm trực tiếp từ trang danh mục
# -------------------------
def test_remove_product_from_inventory(driverLogin):
    wait = WebDriverWait(driverLogin, 10)

    # Thêm sản phẩm
    driverLogin.find_element(By.ID, "add-to-cart-sauce-labs-backpack").click()

    # Kiểm tra số lượng giỏ hàng = 1
    cart_badge = wait.until(
        EC.visibility_of_element_located((By.CLASS_NAME, "shopping_cart_badge"))
    )
    assert cart_badge.text == "1"

    # Nhấn nút Remove trực tiếp trên trang danh mục
    remove_button = driverLogin.find_element(By.ID, "remove-sauce-labs-backpack")
    remove_button.click()

    # Kiểm tra giỏ hàng giảm = 0 (biểu tượng giỏ mất)
    cart_badges = driverLogin.find_elements(By.CLASS_NAME, "shopping_cart_badge")
    assert len(cart_badges) == 0

