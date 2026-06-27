from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.edge.service import Service
from webdriver_manager.microsoft import EdgeChromiumDriverManager

def test_form_validation():
    driver = webdriver.Edge(service=Service(EdgeChromiumDriverManager().install()))
    driver.get("https://bonigarcia.dev/selenium-webdriver-java/data-types.html")
    wait = WebDriverWait(driver, 40)

    # Ждём загрузки страницы
    wait.until(EC.presence_of_element_located((By.TAG_NAME, "body")))

    # Данные для заполнения (Zip code оставляем пустым)
    fields = {
        "first-name": "Иван",
        "last-name": "Петров",
        "address": "Ленина, 55-3",
        "e-mail": "test@skypro.com",
        "phone": "+7985899998787",
        "zip-code": "",
        "city": "Москва",
        "country": "Россия",
        "job-position": "QA",
        "company": "SkyPro"
    }

    # Заполняем каждое поле
    for name, value in fields.items():
        input_field = wait.until(EC.presence_of_element_located((By.NAME, name)))
        input_field.send_keys(value) 

    # Нажимаем Submit
    submit_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[@type='submit']")))
    submit_button.click()

    # Ждём появления красной подсветки (валидация сработала)
    wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, ".alert-danger")))

    # Проверяем, что ровно 1 элемент красный (Zip code)
    red_elements = driver.find_elements(By.CSS_SELECTOR, ".alert-danger")
    assert len(red_elements) == 1, f"Ожидался 1 красный элемент, найдено {len(red_elements)}"

    # Проверяем, что ровно 9 элементов зелёные (все остальные поля)
    green_elements = driver.find_elements(By.CSS_SELECTOR, ".alert-success")
    assert len(green_elements) == 9, f"Ожидалось 9 зелёных элементов, найдено {len(green_elements)}"

    driver.quit()