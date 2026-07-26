# UI-автотесты с Allure-отчётами (Page Object Model)

Проект содержит два автотеста для проверки функциональности:
- **Калькулятор** (сайт `https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html`)
- **Интернет-магазин** (сайт `https://www.saucedemo.com/`)

Тесты написаны с использованием паттерна **Page Object Model** и оформлены с **Allure** для наглядного отчёта.

---

## Требования

- Python 3.12+
- Браузеры: Google Chrome, Mozilla Firefox (для теста магазина)
- Java 8+ (для работы Allure)
- Allure 

---

## Запуск тестов

- Из корня проекта выполните:
python -m pytest lesson_10/tests/ -v --alluredir=lesson_10/allure-results

-v — подробный вывод.
--alluredir — указывает папку для сохранения результатов Allure.

---

## Сгенерируйте отчёт

- Из корня проекта выполните:
allure generate lesson_10/allure-results -o lesson_10/allure-report --clean

-o lesson_10/allure-report — папка для готового отчёта
--clean — перезаписывает предыдущую версию отчёта.

---

## Просмотрите отчёт

- ИОткройте отчёт в браузере:
allure open lesson_10/allure-report