from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class LoginPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def enter_username(self, username):
        locator = (By.ID, "user-name")
        element = self.wait.until(EC.element_to_be_clickable(locator))
        element.send_keys(username)

    def enter_password(self, password):
        locator = (By.ID, "password")
        element = self.driver.find_element(*locator)
        element.send_keys(password)

    def click_login(self):
        locator = (By.ID, "login-button")
        button = self.driver.find_element(*locator)
        button.click()
