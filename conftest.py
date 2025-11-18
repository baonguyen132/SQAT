import pytest

@pytest.fixture
def input_value():
    input = 39
    return input

#Trong pytest, file conftest.py đóng vai trò đặc biệt q/trong việc
# cung cấp fixtures, hooks và các thiết lập trung cho các test case trong một thư mục cụ thể
# Tên conftest.py là quy ước chuẩn của pytesst