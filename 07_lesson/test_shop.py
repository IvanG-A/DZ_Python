from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.firefox.options import Options
from webdriver_manager.firefox import GeckoDriverManager
from pages.login_page import LoginPage


def test_shop():
    options = Options()
    options.binary_location = r"C:\Program Files\Mozilla Firefox\firefox.exe"
    driver = webdriver.Firefox(
        service=Service(GeckoDriverManager().install()),
        options=options
    )
    try:
        login_page = LoginPage(driver)
        inventory_page = login_page.open().login(
            "standard_user", "secret_sauce"
        )

        inventory_page.add_item_to_cart("Sauce Labs Backpack") \
                     .add_item_to_cart("Sauce Labs Bolt T-Shirt") \
                     .add_item_to_cart("Sauce Labs Onesie")

        cart_page = inventory_page.go_to_cart()
        checkout_page = cart_page.checkout()

        checkout_page.fill_form("Иван", "Петров", "123456")
        total = checkout_page.get_total()

        assert total == 58.29, f"Ожидалось 58.29, получено {total}"
    finally:
        driver.quit()
