import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
import time


class TestCalculator(unittest.TestCase):
    def setUp(self):
        # Настройка Chrome браузера
        chrome_options = Options()
        chrome_options.add_argument("--disable-gpu")
        chrome_options.add_argument("--no-sandbox")

        # Инициализация драйвера
        self.driver = webdriver.Chrome(
            service=Service(ChromeDriverManager().install()),
            options=chrome_options
        )
        self.driver.implicitly_wait(10)
        self.driver.maximize_window()

    def test_calculator(self):
        # Открытие страницы
        self.driver.get("https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html")

        # Установка задержки
        delay_input = self.driver.find_element(By.CSS_SELECTOR, "#delay")
        delay_input.send_keys("45")

        # Нажатие кнопок калькулятора
        self.driver.find_element(By.XPATH, "//button[text()='7']").click()
        self.driver.find_element(By.XPATH, "//button[text()='+']").click()
        self.driver.find_element(By.XPATH, "//button[text()='8']").click()
        self.driver.find_element(By.XPATH, "//button[text()='=']").click()

        # Ждем 45 секунд для получения результата
        time.sleep(45)

        # Получаем результат
        result = self.driver.find_element(By.CSS_SELECTOR, "#result").text

        # Проверяем результат
        self.assertEqual(result, "15", "Результат вычислений не соответствует ожидаемому")

    def tearDown(self):
        # Закрытие браузера
        self.driver.quit()



