from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import time


def main():
    try:
        # Инициализация драйвера Chrome
        driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

        try:
            # Открытие страницы
            driver.get("http://uitestingplayground.com/dynamicid")

            # Максимизация окна браузера
            driver.maximize_window()

            # Ожидание загрузки страницы
            time.sleep(5)

            # Поиск кнопки по классу (так как ID динамический)
            button = driver.find_element(By.CLASS_NAME, "btn-primary")

            # Проверка работы кнопки
            if button:
                # Клик по кнопке
                button.click()
                print("Кнопка нажата успешно")
            # Ждем несколько секунд для визуального подтверждения
            time.sleep(5)

        except Exception as error:
            print(f"Произошла ошибка: {str(error)}")

    finally:
        # Закрытие браузера
        if 'driver' in locals():
            driver.quit()
            print("Браузер закрыт")


if __name__ == "__main__":
    main()
