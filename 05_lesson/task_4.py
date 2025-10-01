from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.common.by import By
import time

def main():
    try:
        # Инициализация драйвера Firefox
        driver = webdriver.Firefox(service=Service(GeckoDriverManager().install()))

        try:
            # Открытие страницы
            driver.get("http://the-internet.herokuapp.com/login")

            # Максимизация окна браузера
            driver.maximize_window()

            # Ожидание загрузки страницы
            time.sleep(3)

            # Поиск полей ввода
            username_field = driver.find_element(By.ID, "username")
            password_field = driver.find_element(By.ID, "password")

            # Ввод данных
            username_field.send_keys("Window_5")
            password_field.send_keys("12345!")

            # Поиск и клик по кнопке входа
            login_button = driver.find_element(By.CSS_SELECTOR, "button[type='submit']")
            login_button.click()

            # Ожидание загрузки страницы после входа
            time.sleep(3)

            # Получение текста с зеленой плашки
            success_message = driver.find_element(By.CSS_SELECTOR, ".flash.success")
            print(f"Сообщение об успехе: {success_message.text}")

        except Exception as e:
            print(f"Произошла ошибка: {str(e)}")

        finally:
            # Закрытие браузера
            if 'driver' in locals():
                driver.quit()
                print("Браузер закрыт")

    except Exception as e:
        print(f"Критическая ошибка: {str(e)}")

if __name__ == "__main__":
    main()
