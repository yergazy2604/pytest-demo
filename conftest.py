import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By

from utilities.test_data import TestData


@pytest.fixture(params=["chrome", "firefox"])
def initialize_driver(request):
    if request.param == "chrome":
        driver = webdriver.Chrome()
    elif request.param == "firefox":
        driver = webdriver.Firefox()    
    request.cls.driver = driver
    print("Browser: ", request.param)
    driver.get(TestData.url)
    driver.maximize_window()
    yield
    print("Close Driver")
    driver.close()