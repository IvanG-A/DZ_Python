from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager


def test_calculator():
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    driver.get("https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html")
    wait = WebDriverWait(driver, 50)  # ждём до 50 секунд

    # Вводим задержку 45
    delay_input = driver.find_element(By.CSS_SELECTOR, "#delay")
    delay_input.clear()
    delay_input.send_keys("45")

    # Нажимаем кнопки: 7, +, 8, =
    driver.find_element(By.XPATH, "//span[text()='7']").click()
    driver.find_element(By.XPATH, "//span[text()='+']").click()
    driver.find_element(By.XPATH, "//span[text()='8']").click()
    driver.find_element(By.XPATH, "//span[text()='=']").click()

    # Ожидаем, что в окне результата появится значение 15
    result_element = wait.until(
        EC.text_to_be_present_in_element((By.CSS_SELECTOR, ".screen"), "15")
    )

    # Дополнительная проверка: получаем текст и сравниваем
    result_text = driver.find_element(By.CSS_SELECTOR, ".screen").text
    assert result_text == "15", f"Ожидалось 15, получено {result_text}"

    driver.quit()