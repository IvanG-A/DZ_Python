from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class LoginPage:
    """Page Object для страницы авторизации."""

    def __init__(self, driver):
        """
        Инициализация страницы авторизации.

        :param driver: WebDriver экземпляр.
        """
        self.driver = driver
        self.wait = WebDriverWait(driver, 30)

    def open(self) -> "LoginPage":
        """
        Открывает страницу авторизации.

        :return: Объект текущей страницы для цепочки вызовов.
        """
        self.driver.get("https://www.saucedemo.com/")
        return self

    def login(self, username: str, password: str) -> "InventoryPage":
        """
        Выполняет вход в систему с указанными учётными данными.

        :param username: Имя пользователя (логин).
        :param password: Пароль.
        :return: Объект главной страницы (InventoryPage).
        """
        self.wait.until(
            EC.presence_of_element_located((By.ID, "user-name"))
        ).send_keys(username)
        self.driver.find_element(By.ID, "password").send_keys(password)
        self.driver.find_element(By.ID, "login-button").click()
        from pages.inventory_page import InventoryPage
        return InventoryPage(self.driver)