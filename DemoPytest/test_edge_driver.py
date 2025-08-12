from selenium import webdriver
from selenium.webdriver.edge.service import Service
from selenium.webdriver.edge.options import Options

options = Options()
options.add_argument("--start-maximized")

def test_edge():
    driver = webdriver.Edge(options=options)
    driver.get("https://www.google.com")
    print(driver.title)
    driver.quit()