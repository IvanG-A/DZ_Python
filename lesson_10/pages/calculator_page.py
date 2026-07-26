from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class CalculatorPage:
    """Page Object для страницы калькулятора (медленный калькулятор)."""

    def __init__(self, driver):
        """
        Инициализация страницы калькулятора.

        :param driver: WebDriver экземпляр.
        """
        self.driver = driver
        self.wait = WebDriverWait(driver, 60)

    def open(self) -> "CalculatorPage":
        """
        Открывает страницу калькулятора.

        :return: Объект текущей страницы для цепочки вызовов.
        """
        self.driver.get(
            "https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html"
        )
        return self

    def set_delay(self, seconds: str) -> None:
        """
        Устанавливает задержку перед вычислением.

        :param seconds: Количество секунд (строка).
        """
        delay_input = self.wait.until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "#delay"))
        )
        delay_input.clear()
        delay_input.send_keys(seconds)

    def press_button(self, button_text: str) -> None:
        """
        Нажимает кнопку на калькуляторе.

        :param button_text: Текст на кнопке (например, '7', '+', '=').
        """
        button = self.wait.until(
            EC.element_to_be_clickable(
                (By.XPATH, f"//span[text()='{button_text}']")
            )
        )
        button.click()

    def wait_for_result(self, expected_text: str) -> None:
        """
        Ожидает, пока в поле результата появится заданный текст.

        :param expected_text: Ожидаемый текст результата.
        """
        self.wait.until(
            EC.text_to_be_present_in_element(
                (By.CSS_SELECTOR, ".screen"), expected_text
            )
        )

    def get_result(self) -> str:
        """
        Получает текущий текст результата.

        :return: Текст результата (строка).
        """
        return self.driver.find_element(By.CSS_SELECTOR, ".screen").text