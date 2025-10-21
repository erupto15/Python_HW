from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class CalculatorPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 60) # ожидание до 60 сек

        # локаторы элементов
        self.delay_input = (By.ID, "delay")
        self.button_7 = (By.XPATH, "//span[text()='7']")
        self.button_plus = (By.XPATH, "//span[text()='+']")
        self.button_8 = (By.XPATH, "//span[text()='8']")
        self.button_equals = (By.XPATH, "//span[text()='=']")
        self.result_screen = (By.CLASS_NAME, "screen")

    def set_delay (self, seconds):
        element = self.driver.find_element(*self.delay_input)
        element.clear()
        element.send_keys(str(seconds))

    def click_seven(self):
        # Нажатие кнопки 7
        self.driver.find_element(*self.button_7).click()

    def click_plus(self):
        # нажатие кнопки плюс
        self.driver.find_element(*self.button_plus).click()

    def click_eight(self):
        # Нажатие кнопки 8
        self.driver.find_element(*self.button_8).click()

    def click_equals(self):
        # Нажатие кнопки
        self.driver.find_element(*self.button_equals).click()

    def get_result(self):
        """Получение результата с ожиданием"""
        result_element = self.wait.until(
            EC.text_to_be_present_in_element(self.result_screen, "15")
        )


        return self.driver.find_element(*self.result_screen).text