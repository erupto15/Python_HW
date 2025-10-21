from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class LoginPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def enter_username(self, username):
        """
        Ввести имя пользователя в поле логина.

        Args:
            username (str): Имя пользователя
        """
        locator = (By.ID, "user-name")
        element = self.wait.until(EC.element_to_be_clickable(locator))
        element.clear()  # Очистка поля
        element.send_keys(username)

    def enter_password(self, password):

        """Ввести пароль в поле ввода.

        Args:
            password (str): Пароль
        """
        locator = (By.ID, "password")
        element = self.wait.until(EC.element_to_be_clickable(locator))
        element.clear()  # Очистка поля
        element.send_keys(password)

    def click_login(self):
        """
        Нажать кнопку входа в систему.
        """
        locator = (By.ID, "login-button")
        button = self.wait.until(EC.element_to_be_clickable(locator))
        button.click()

