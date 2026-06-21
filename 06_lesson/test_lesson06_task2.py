from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_session_storage_auth():
    driver = webdriver.Chrome()

    # 1. Откройте страницу https://gitflic.ru/
    driver.get("https://gitflic.ru/")
    print("Открыта главная страница")

    # 2. Установите cookie пользователя 1
    user1_cookie = {
        "name": "session",
        "value": "ZmFiZGVkZmEtMTgzMC00OWU2LWFhNTUtYWY1OTRhMDhkZDQ3",
        "domain": "gitflic.ru",
        "path": "/"
    }
    driver.add_cookie(user1_cookie)
    print("Cookie пользователя 1 установлены")

    # 3. Обновите страницу
    driver.refresh()
    print("Страница обновлена")

    # 4. Перейдите на страницу пользователя 1
    user1_url = "https://gitflic.ru/user/ivantest1"
    driver.get(user1_url)
    print(f"Переход на страницу пользователя 1: {user1_url}")

    # 5. Сохраните текущий URL
    url_user1 = driver.current_url
    print(f"URL пользователя 1: {url_user1}")

    # 6. Разлогиньтесь (очистите куки)
    driver.delete_all_cookies()
    print("Все cookie очищены")

    # 7. Установите cookie пользователя 2
    user2_cookie = {
        "name": "session",
        "value": "N2U1ZjU2ODUtOGNjNi00YTdkLWFlMDUtODVhMjgyNzZlMTlj",
        "domain": "gitflic.ru",
        "path": "/"
    }
    driver.add_cookie(user2_cookie)
    print("Cookie пользователя 2 установлены")

    # 8. Обновите страницу
    driver.refresh()
    print("Страница обновлена")

    # 9. Перейдите на страницу пользователя 2
    user2_url = "https://gitflic.ru/user/ivantest2"
    driver.get(user2_url)
    print(f"Переход на страницу пользователя 2: {user2_url}")

    # 10. Сохраните текущий URL
    url_user2 = driver.current_url
    print(f"URL пользователя 2: {url_user2}")

    # 11. Проверьте, что URL разных пользователей различаются
    assert url_user1 != url_user2, f"URL одинаковые: {url_user1}"
    print("✅ Тест пройден: URL разных пользователей отличаются")

    driver.quit()