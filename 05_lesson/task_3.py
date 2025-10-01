from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from webdriver_manager.firefox import GeckoDriverManager
import time


def main():
    try:
        # Инициализация драйвера Firefox
        driver = webdriver.Firefox(service=Service(GeckoDriverManager().install()))

        try:
            # Открытие страницы
            driver.get("http://the-internet.herokuapp.com/inputs")

            # Максимизация окна браузера
            driver.maximize_window()

            # Ожидание загрузки страницы
            time.sleep(2)

            # Поиск поля ввода
            input_field = driver.find_element("xpath", "//input[@type='text']")

            # Шаг 1: Ввод текста "Sky"
            input_field.send_keys("Sky")
            print("Введено значение 'Sky'")
            time.sleep(3)

            # Шаг 2: Очистка поля
            input_field.clear()
            print("Поле очищено")
            time.sleep(1)

            # Шаг 3: Ввод текста "Pro"
            input_field.send_keys("Pro")
            print("Введено значение 'Pro'")
            time.sleep(3)

        except Exception as error:
            print(f"Произошла ошибка: {str(error)}")

    finally:
        # Закрытие браузера
        if 'driver' in locals():
            driver.quit()
            print("Браузер закрыт")


if __name__ == "__main__":
    main()
