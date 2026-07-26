from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class InventoryPage:
    """Page Object для главной страницы магазина (инвентарь)."""

    def __init__(self, driver):
        """
        Инициализация страницы инвентаря.

        :param driver: WebDriver экземпляр.
        """
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def add_item_to_cart(self, item_name: str) -> "InventoryPage":
        """
        Добавляет товар с указанным названием в корзину.

        :param item_name: Название товара (например, 'Sauce Labs Backpack').
        :return: Объект текущей страницы для цепочки вызовов.
        """
        add_button = self.wait.until(
            EC.element_to_be_clickable(
                (
                    By.XPATH,
                    f"//div[text()='{item_name}']/ancestor::"
                    f"div[@class='inventory_item']//button"
                )
            )
        )
        add_button.click()
        return self

    def go_to_cart(self) -> "CartPage":
        """
        Переходит в корзину.

        :return: Объект страницы корзины (CartPage).
        """
        self.driver.find_element(By.CLASS_NAME, "shopping_cart_link").click()
        from pages.cart_page import CartPage
        return CartPage(self.driver)