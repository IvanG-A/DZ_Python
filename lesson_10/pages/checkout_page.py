from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class CheckoutPage:
    """Page Object для страницы оформления заказа."""

    def __init__(self, driver):
        """
        Инициализация страницы оформления заказа.

        :param driver: WebDriver экземпляр.
        """
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def fill_form(self, first_name: str, last_name: str, postal_code: str) -> "CheckoutPage":
        """
        Заполняет форму оформления заказа и нажимает кнопку "Continue".

        :param first_name: Имя.
        :param last_name: Фамилия.
        :param postal_code: Почтовый индекс.
        :return: Объект текущей страницы для цепочки вызовов.
        """
        self.wait.until(
            EC.element_to_be_clickable((By.ID, "first-name"))
        ).send_keys(first_name)
        self.wait.until(
            EC.element_to_be_clickable((By.ID, "last-name"))
        ).send_keys(last_name)
        self.wait.until(
            EC.element_to_be_clickable((By.ID, "postal-code"))
        ).send_keys(postal_code)
        self.wait.until(
            EC.element_to_be_clickable((By.ID, "continue"))
        ).click()
        return self

    def get_total(self) -> float:
        """
        Получает итоговую стоимость заказа.

        :return: Итоговая сумма (float).
        """
        total_element = self.wait.until(
            EC.presence_of_element_located(
                (By.CSS_SELECTOR, ".summary_total_label")
            )
        )
        total_text = total_element.text
        return float(total_text.replace("Total: $", ""))