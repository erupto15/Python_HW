import unittest
from selenium import webdriver
from calculator_page import CalculatorPage

class TestCalculator(unittest.TestCase):
    def setUp(self):
        # Инициализация драйвера (пример для Chrome)
        self.driver = webdriver.Chrome()
        self.driver.get("https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html")
        self.calculator = CalculatorPage(self.driver)

    def tearDown(self):
        # Закрытие браузера после теста
        self.driver.quit()

    def test_addition(self):
        # Шаг 1: Ввод задержки 45 секунд
        self.calculator.set_delay(45)

        # Шаг 2: Нажатие кнопок 7, +, 8, =
        self.calculator.click_seven()
        self.calculator.click_plus()
        self.calculator.click_eight()
        self.calculator.click_equals()

        # Шаг 3: Проверка результата
        result = self.calculator.get_result()
        self.assertEqual(result, "15", "Результат должен быть равен 15")


