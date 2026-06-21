from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_dynamic_loading():
    driver = webdriver.Chrome()

    # 1. Откройте страницу
    driver.get("https://the-internet.herokuapp.com/dynamic_loading/2")

    # 2. Найдите и нажмите на кнопку "Start" (используем CSS-селектор)
    start_button = driver.find_element(By.CSS_SELECTOR, "#start button")
    start_button.click()

    # 3. Дождитесь появления текста "Hello World!" (явное ожидание)
    hello_text_element = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, "#finish h4"))
    )

    # 4. Сделайте скриншот страницы
    driver.save_screenshot("dynamic_loading_success.png")
    print("📸 Скриншот сохранён как dynamic_loading_success.png")

    # 5. Проверьте, что появившийся текст равен "Hello World!"
    actual_text = hello_text_element.text
    assert actual_text == "Hello World!", f"Ожидалось 'Hello World!', получено '{actual_text}'"

    driver.quit()