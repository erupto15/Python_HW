from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class CheckoutPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def fill_personal_info(self, first_name, last_name, zip_code):
        first_name_field = self.driver.find_element(By.ID, "first-name")
        first_name_field.send_keys(first_name)

        last_name_field = self.driver.find_element(By.ID, "last-name")
        last_name_field.send_keys(last_name)

        zip_code_field = self.driver.find_element(By.ID, "postal-code")
        zip_code_field.send_keys(zip_code)

    def click_continue(self):
        locator = (By.ID, "continue")
        button = self.driver.find_element(*locator)
        button.click()

    def get_total_price(self):
        locator = (By.CLASS_NAME, "summary_total_label")
        price_element = self.wait.until(EC.visibility_of_element_located(locator))
        return price_element.text  # Например: "$58.29"
