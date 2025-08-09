import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time


def test_ddlog_homepage():
    driver = webdriver.Chrome()
    driver.maximize_window()
    try:
        driver.get("https://ddlog.test.ddirection.kz/")
        print("Title: ", driver.title)

        wait = WebDriverWait(driver, 10)
        wait.until(EC.title_is("Авторизация"))
        expected_title = "Авторизация"
        actual_title = driver.title

        print(f"Expected Title: {expected_title}")
        print(f"Actual Title: {actual_title}")

        assert actual_title == expected_title, f"Заголовок страницы не соответствует ожидаемому. Ожидалось: '{expected_title}', Получено: '{actual_title}'"

    except Exception as e:
        pytest.fail(f"Тест не выполнен из-за ошибки: {e}")
    finally:
        driver.quit()

