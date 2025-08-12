import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By


@pytest.fixture(params=["chrome", "firefox"])
def initialize_driver(request):
    if request.param == "chrome":
        driver = webdriver.Chrome()
    elif request.param == "firefox":
        driver = webdriver.Firefox()    
    request.cls.driver = driver
    print("Browser: ", request.param)
    yield
    print("Close Driver")
    driver.close()