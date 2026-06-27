from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.firefox.service import Service
from webdriver_manager.firefox import GeckoDriverManager


def test_shopping():
    driver = webdriver.Firefox(service=Service(GeckoDriverManager().install()))
    driver.get("https://www.saucedemo.com/")
    wait = WebDriverWait(driver, 40)

    # Авторизация
    driver.find_element(By.ID, "user-name").send_keys("standard_user")
    driver.find_element(By.ID, "password").send_keys("secret_sauce")
    driver.find_element(By.ID, "login-button").click()

    # Добавляем товары в корзину
    items = ["Sauce Labs Backpack", "Sauce Labs Bolt T-Shirt", "Sauce Labs Onesie"]
    for item in items:
        # Находим кнопку добавления для каждого товара (используем частичный текст)
        add_button = driver.find_element(By.XPATH, f"//div[text()='{item}']/ancestor::div[@class='inventory_item']//button")
        add_button.click()

    # Переходим в корзину
    driver.find_element(By.CLASS_NAME, "shopping_cart_link").click()

    # Оформляем заказ
    driver.find_element(By.ID, "checkout").click()

    # Заполняем форму
    driver.find_element(By.ID, "first-name").send_keys("Иван")
    driver.find_element(By.ID, "last-name").send_keys("Петров")
    driver.find_element(By.ID, "postal-code").send_keys("123456")
    driver.find_element(By.ID, "continue").click()

    # Ожидаем появления итоговой суммы
    total_element = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, ".summary_total_label")))
    total_text = total_element.text
    # Извлекаем числовое значение (например, "Total: $58.29" -> 58.29)
    total_value = float(total_text.replace("Total: $", ""))

    # Проверяем, что итоговая сумма равна 58.29
    assert total_value == 58.29, f"Ожидалось 58.29, получено {total_value}"

    driver.quit()