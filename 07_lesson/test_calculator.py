import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from pages.calculator_page import CalculatorPage

def test_calculator():
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    try:
        calc_page = CalculatorPage(driver)
        calc_page.open()
        calc_page.set_delay("45")
        calc_page.press_button("7")
        calc_page.press_button("+")
        calc_page.press_button("8")
        calc_page.press_button("=")

        # Ждём, пока результат станет "15"
        calc_page.wait_for_result("15")
        result = calc_page.get_result()
        assert result == "15", f"Ожидалось 15, получено {result}"
    finally:
        driver.quit()