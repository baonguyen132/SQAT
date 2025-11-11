from selenium import webdriver
import time

if __name__ == '__main__':
    driver = webdriver.Chrome()
    driver.get("https://the-internet.herokuapp.com/login")

    username = driver.find_element("id" , "username")
    password = driver.find_element("id", "password")
    login = driver.find_element("css selector", "button[type='submit']")

    username.send_keys("tomsmith")
    password.send_keys("SuperSecretPassword!")

    login.click()

    message = driver.find_element("id", "flash")
    print(message.text)

    # time.sleep(5)
    #
    # next_button = driver.find_element("name", "username")
    #
    # print("Text của nút Next là: ", next_button.get_attribute("value"))
    #
    # next_button.click()
    #
    # time.sleep(3)
    #
    # driver.quit()