from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class InventoryPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def add_item_to_cart(self, item_name: str):
        # Формируем XPath для кнопки добавления товара по его названию
        add_button = self.wait.until(EC.element_to_be_clickable(
            (By.XPATH, f"//div[text()='{item_name}']/ancestor::div[@class='inventory_item']//button")
        ))
        add_button.click()
        return self

    def go_to_cart(self):
        self.driver.find_element(By.CLASS_NAME, "shopping_cart_link").click()
        from pages.cart_page import CartPage
        return CartPage(self.driver)