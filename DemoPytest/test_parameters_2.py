import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By



@pytest.mark.usefixtures("initialize_driver")
class BaseClass:
    pass

class TestDrivers(BaseClass):
    def test_multiple_browsers(self):
        self.driver.get("https://www.lambdatest.com/selenium-playground/")
        header = self.driver.find_element(By.XPATH, "//*[@id='__next']/div/section[1]/div/h1").text
        print("Header: ", header)
        assert header == "Selenium Playground"