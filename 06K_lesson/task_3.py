# test_03_shop.py

import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.firefox.options import Options
from webdriver_manager.firefox import GeckoDriverManager
import time


class TestShop(unittest.TestCase):
    def setUp(self):
        # Настройка Firefox браузера
        firefox_options = Options()
        firefox_options.add_argument("--disable-extensions")
        firefox_options.add_argument("--disable-gpu")

        # Инициализация драйвера
        self.driver = webdriver.Firefox(
            service=Service(GeckoDriverManager().install()),
            options=firefox_options
        )
        self.driver.implicitly_wait(10)
        self.driver.maximize_window()

    def test_shopping(self):
        # Открытие страницы магазина
        self.driver.get("https://www.saucedemo.com/")

        # Авторизация
        self.driver.find_element(By.ID, "user-name").send_keys("standard_user")
        self.driver.find_element(By.ID, "password").send_keys("secret_sauce")
        self.driver.find_element(By.ID, "login-button").click()

        # Добавление товаров в корзину
        self.driver.find_element(By.XPATH,
                                 "//div[contains(text(),'Sauce Labs Backpack')]/following-sibling::button").click()
        self.driver.find_element(By.XPATH,
                                 "//div[contains(text(),'Sauce Labs Bolt T-Shirt')]/following-sibling::button").click()
        self.driver.find_element(By.XPATH,
                                 "//div[contains(text(),'Sauce Labs Onesie')]/following-sibling::button").click()

        # Переход в корзину
        self.driver.find_element(By.CSS_SELECTOR, "#shopping_cart_link").click()
        self.driver.find_element(By.CSS_SELECTOR, "#checkout").click()

        # Заполнение формы
        self.driver.find_element(By.ID, "first-name").send_keys("Иван")
        self.driver.find_element(By.ID, "last-name").send_keys("Петров")
        self.driver.find_element(By.ID, "postal-code").send_keys("12345")
        self.driver.find_element(By.CSS_SELECTOR, "#continue").click()

        # Получение итоговой стоимости
        total_amount = self.driver.find_element(By.CSS_SELECTOR, "#total_amount").text

        # Проверка суммы
        self.assertEqual(total_amount, "$58.29", "Итоговая сумма не соответствует ожидаемой")

    def tearDown(self):
        # Закрытие браузера
        self.driver.quit()


