from selenium import webdriver

def test_lambdatest_playground():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get("https://www.lambdatest.com/selenium-playground/")
    print("Title:", driver.title)

def test_lambdatest_ecommerce():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get("https://ecommerce-playground.lambdatest.io/")
    print("Title:", driver.title)

def test_rex_website():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get("https://www.rexjones2.com/")
    print("Title:", driver.title)

def test_google():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get("https://www.google.com/")
    print("Title:", driver.title)