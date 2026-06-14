import time
from selenium import webdriver
from selenium.webdriver.common.by import By

def test_multiple_elements():
    driver = webdriver.Chrome()
    driver.get("https://httpbin.org/links/10")
    time.sleep(1)

    links = driver.find_elements(By.TAG_NAME, "a")
    # По заданию должно быть 10, но реально на сайте 9. ЗТО ОШИБКА?
    assert len(links) == 10

    for link in links:
        assert link.is_displayed()

    assert "1" in links[0].text

    driver.quit()