import time
from selenium import webdriver
from selenium.webdriver.common.by import By

def test_form_submission():
    driver = webdriver.Chrome()
    driver.get("https://httpbin.org/forms/post")
    time.sleep(1)

    # Поле ввода "custname"
    name_field = driver.find_element(By.NAME, "custname")
    name_field.send_keys("Иван")
    time.sleep(1)

    # Кнопка "Submit order" (ищем по части текста)
    submit_button = driver.find_element(By.XPATH, "//button[contains(text(), 'Submit')]")
    original_url = driver.current_url
    submit_button.click()
    time.sleep(1)

    # Проверяем, что URL изменился
    assert driver.current_url != original_url

    driver.quit()