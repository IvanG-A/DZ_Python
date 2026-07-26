import allure
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from pages.calculator_page import CalculatorPage


@allure.feature("Калькулятор")
@allure.story("Проверка медленного калькулятора")
@allure.title("Вычисление 7 + 8 с задержкой 45 секунд")
@allure.description("Тест проверяет, что калькулятор корректно вычисляет сумму с учётом задержки.")
@allure.severity(allure.severity_level.CRITICAL)
def test_calculator():
    with allure.step("Запуск браузера и открытие страницы калькулятора"):
        driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        calc_page = CalculatorPage(driver)
        calc_page.open()

    with allure.step("Установка задержки 45 секунд"):
        calc_page.set_delay("45")

    with allure.step("Нажатие кнопок: 7, +, 8, ="):
        calc_page.press_button("7")
        calc_page.press_button("+")
        calc_page.press_button("8")
        calc_page.press_button("=")

    with allure.step("Ожидание появления результата '15'"):
        calc_page.wait_for_result("15")

    with allure.step("Проверка результата"):
        result = calc_page.get_result()
        assert result == "15", f"Ожидалось 15, получено {result}"

    with allure.step("Закрытие браузера"):
        driver.quit()