import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

@pytest.fixture()
def setup_teardown():
    driver.get("https://ecommerce-playground.lambdatest.io/index.php?route=account/login")
    driver.find_element(By.ID, "input-email").send_keys("yergazy.nur@yandex.kz")
    driver.find_element(By.ID, "input-password").send_keys("Qwerty123")
    driver.find_element(By.XPATH, "//input[@value='Login']").click()    
    print("Log In")
    yield
    driver.find_element(By.LINK_TEXT, "Logout").click()
    print("Log Out")

def test_order_history_title(setup_teardown):
    
    driver.find_element(By.LINK_TEXT, "Order History").click()
    assert driver.title == "Order History"
    print("Test 1 is complete")

def test_change_password_title(setup_teardown):
    driver.find_element(By.LINK_TEXT, "Password").click()
    assert driver.title == "Change Password"
    print("Test 2 is complete")