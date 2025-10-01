import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By



class TestClickButtonWithCSSClass:
    def setup_method(self):
        # Инициализация драйвера Chrome
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.driver.maximize_window()

    def teardown_method(self):
        # Закрытие браузера после каждого теста
        if self.driver:
            self.driver.quit()

    def test_click_button(self):
        try:
            # Открытие страницы
            self.driver.get("http://uitestingplayground.com/classattr")

            # Ожидание загрузки страницы
            time.sleep(2)

            # Поиск кнопки по классу
            button = self.driver.find_element(By.CLASS_NAME, "btn-primary")

            # Проверка наличия кнопки
            assert button is not None, "Кнопка не найдена"

            # Клик по кнопке
            button.click()
            print("Кнопка нажата успешно")

            # Ждем несколько секунд для визуального подтверждения
            time.sleep(3)

        except Exception as e:
            print(f"Произошла ошибка: {str(e)}")
            raise



