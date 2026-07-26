from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class CartPage:
    """Page Object для страницы корзины."""

    def __init__(self, driver):
        """
        Инициализация страницы корзины.

        :param driver: WebDriver экземпляр.
        """
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def checkout(self) -> "CheckoutPage":
        """
        Нажимает кнопку "Checkout" для перехода к оформлению заказа.

        :return: Объект страницы оформления заказа (CheckoutPage).
        """
        self.wait.until(
            EC.element_to_be_clickable((By.ID, "checkout"))
        ).click()
        from pages.checkout_page import CheckoutPage
        return CheckoutPage(self.driver)