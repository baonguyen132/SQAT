from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select

def test_sort_products(driverLogin):
    wait = WebDriverWait(driverLogin, 10)

    # Đợi dropdown sort xuất hiện
    sort_select = wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "product_sort_container")))
    select = Select(sort_select)

    # 1️⃣ Sắp xếp theo "Tên (A-Z)"
    select.select_by_value("az")  # Giá trị của option trên SauceDemo
    wait.until(lambda d: d.find_element(By.CLASS_NAME, "inventory_item_name"))  # chờ load lại

    # Lấy danh sách tên sản phẩm
    product_names = [e.text for e in driverLogin.find_elements(By.CLASS_NAME, "inventory_item_name")]
    assert product_names == sorted(product_names), "Tên sản phẩm chưa sắp xếp A-Z"

    # 2️⃣ Sắp xếp theo "Giá (Thấp → Cao)"
    select.select_by_value("lohi")  # Giá trị option cho giá tăng dần
    wait.until(lambda d: d.find_element(By.CLASS_NAME, "inventory_item_price"))

    # Lấy danh sách giá sản phẩm
    prices = [float(e.text.replace("$", "")) for e in driverLogin.find_elements(By.CLASS_NAME, "inventory_item_price")]
    assert prices == sorted(prices), "Giá sản phẩm chưa sắp xếp từ thấp đến cao"