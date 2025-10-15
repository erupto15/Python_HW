import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager


class TestCalculator(unittest.TestCase):
    def setUp(self):
        # Настройка Chrome браузера
        chrome_options = ChromeOptions()
        chrome_options.add_argument("--disable-gpu")
        chrome_options.add_argument("--no-sandbox")
        chrome_options.add_argument("--disable-dev-shm-usage")  # Для Docker
        chrome_options.add_argument("--headless")  # Для запуска в headless режиме

        # Инициализация драйвера
        self.driver = webdriver.Chrome(
            service=ChromeService(ChromeDriverManager().install()),
            options=chrome_options
        )
        self.driver.implicitly_wait(10)  # Неявное ожидание
        self.driver.maximize_window()

    def test_calculator(self):
        # Открытие страницы
        self.driver.get("https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html")

        # Дожидаемся полной загрузки калькулятора
        WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located((By.ID, "delay"))
        )

        # Устанавливаем задержку в 45 секунд
        self.driver.find_element(By.ID, "delay").send_keys("45")

        # Нажимаем кнопки калькулятора
        self.driver.find_element(By.XPATH, "//button[text()='7']").click()
        self.driver.find_element(By.XPATH, "//button[text()='+']").click()
        self.driver.find_element(By.XPATH, "//button[text()='8']").click()
        self.driver.find_element(By.XPATH, "//button[text()='=']").click()

        # Ждем результата с учетом задержки
        try:
            result = WebDriverWait(self.driver, 60).until(
                EC.text_to_be_present_in_element((By.ID, "result"), "15")
            )
            self.assertEqual(result, "15", "Результат не совпадает с ожидаемым")
        except Exception as e:
            print(f"Произошла ошибка: {str(e)}")
            self.fail("Тест не прошел")

    def tearDown(self):
        # Закрытие браузера
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()


