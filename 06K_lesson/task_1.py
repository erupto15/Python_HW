# test_01_form.py

import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.edge.service import Service as EdgeService
from selenium.webdriver.edge.options import Options as EdgeOptions
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.microsoft import EdgeChromiumDriverManager


class TestFormFilling(unittest.TestCase):
    def setUp(self):
        # Настройка Edge браузера
        edge_options = EdgeOptions()
        edge_options.use_chromium = True
        edge_options.add_argument("--disable-gpu")
        edge_options.add_argument("--no-sandbox")
        edge_options.add_argument("--disable-dev-shm-usage")  # Для Docker
        edge_options.add_argument("--headless")  # Для запуска в headless режиме

        # Инициализация драйвера
        self.driver = webdriver.Edge(
            service=EdgeService(EdgeChromiumDriverManager().install()),
            options=edge_options
        )
        self.driver.implicitly_wait(10)  # Неявное ожидание
        self.driver.maximize_window()

    def test_fill_form(self):
        # Открытие страницы
        self.driver.get("https://bonigarcia.dev/selenium-webdriver-java/data-types.html")

        # Дожидаемся полной загрузки формы
        WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located((By.NAME, "firstname"))
        )

        # Заполнение формы
        self.driver.find_element(By.NAME, "firstname").send_keys("Иван")
        self.driver.find_element(By.NAME, "lastname").send_keys("Петров")
        self.driver.find_element(By.NAME, "address").send_keys("Ленина, 55-3")
        self.driver.find_element(By.NAME, "email").send_keys("test@skypro.com")
        self.driver.find_element(By.NAME, "phone").send_keys("+7985899998787")
        # Zip code оставляем пустым
        self.driver.find_element(By.NAME, "city").send_keys("Москва")
        self.driver.find_element(By.NAME, "country").send_keys("Россия")
        self.driver.find_element(By.NAME, "position").send_keys("QA")
        self.driver.find_element(By.NAME, "company").send_keys("SkyPro")

        # Отправка формы
        self.driver.find_element(By.NAME, "submit").click()

        # Дожидаемся валидации
        WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located((By.NAME, "zipcode"))
        )

        # Проверяем, что zip code красный
        zip_code_input = self.driver.find_element(By.NAME, "zipcode")
        self.assertIn("invalid", zip_code_input.get_attribute("class"),
                     "Поле zip code не подсвечено красным")

        # Проверяем, что остальные поля зеленые
        green_fields = [
            "firstname", "lastname", "address", "email", "phone",
            "city", "country", "position", "company"
        ]

        for field in green_fields:
            element = self.driver.find_element(By.NAME, field)
            self.assertIn("valid", element.get_attribute("class"),
                         f"Поле {field} не подсвечено зеленым")

    def tearDown(self):
        # Закрытие браузера
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()
