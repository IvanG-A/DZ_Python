import allure
from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.firefox.options import Options
from webdriver_manager.firefox import GeckoDriverManager
from pages.login_page import LoginPage


@allure.feature("Интернет-магазин")
@allure.story("Оформление заказа")
@allure.title("Проверка итоговой суммы заказа")
@allure.description("Тест проверяет, что итоговая сумма заказа равна $58.29.")
@allure.severity(allure.severity_level.CRITICAL)
def test_shop():
    with allure.step("Настройка и запуск Firefox"):
        options = Options()
        options.binary_location = r"C:\Program Files\Mozilla Firefox\firefox.exe"
        driver = webdriver.Firefox(service=Service(GeckoDriverManager().install()), options=options)

    with allure.step("Открытие страницы авторизации и вход"):
        login_page = LoginPage(driver)
        inventory_page = login_page.open().login("standard_user", "secret_sauce")

    with allure.step("Добавление товаров в корзину"):
        inventory_page.add_item_to_cart("Sauce Labs Backpack") \
                     .add_item_to_cart("Sauce Labs Bolt T-Shirt") \
                     .add_item_to_cart("Sauce Labs Onesie")

    with allure.step("Переход в корзину и оформление заказа"):
        cart_page = inventory_page.go_to_cart()
        checkout_page = cart_page.checkout()

    with allure.step("Заполнение формы заказа"):
        checkout_page.fill_form("Иван", "Петров", "123456")

    with allure.step("Получение итоговой суммы"):
        total = checkout_page.get_total()

    with allure.step("Проверка итоговой суммы"):
        assert total == 58.29, f"Ожидалось 58.29, получено {total}"

    with allure.step("Закрытие браузера"):
        driver.quit()