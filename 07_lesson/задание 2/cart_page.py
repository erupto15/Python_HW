from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class CartPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def click_checkout(self):
        locator = (By.ID, "checkout")
        button = self.wait.until(EC.element_to_be_clickable(locator))
        button.click()

    def get_cart_items(self):
        # Для проверки содержимого корзины (опционально)
        locator = (By.CLASS_NAME, "cart_item")
        return self.driver.find_elements(*locator)

    def get_cart_items_count(self):
        """Получить количество товаров в корзине"""
        locator = (By.CLASS_NAME, "cart_item")
        items = self.wait.until(EC.presence_of_all_elements_located(locator))
        return len(items)

    def is_empty(self):
        """
        Проверить, пуста ли корзина.
        Возвращает True, если товаров нет.
        """
        try:
            self.wait.until(EC.invisibility_of_element_located((By.CLASS_NAME, "cart_item")))
            return True
        except:
            return len(self.get_cart_items()) == 0


