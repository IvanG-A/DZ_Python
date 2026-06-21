import time
from selenium import webdriver
from selenium.webdriver.common.by import By

def test_navigation():
    driver = webdriver.Chrome()
    driver.get("https://httpbin.org/")
    time.sleep(1)

    # Ищем ссылку по адресу
    link = driver.find_element(By.XPATH, "//a[contains(@href, '/forms/post')]")
    link.click()
    time.sleep(1)

    # Проверяем, что URL изменился на /forms/post
    assert driver.current_url == "https://httpbin.org/forms/post"

    driver.back()
    time.sleep(1)

    assert driver.current_url == "https://httpbin.org/"

    driver.quit()