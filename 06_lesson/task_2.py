from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

driver = webdriver.Chrome()

#Шаг 1. Переходим на страницу сайта
driver.get('http://uitestingplayground.com/ajax')

# Шаг 2: Ввод текста в поле
input_field = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, 'input'))
)
input_field.send_keys('SkyPro')

#Шаг 3. Нажать на синюю кнопку
button = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.CSS_SELECTOR, 'button'))
)
button.click()

# Шаг 4. Получение текста кнопки
updated_button_text = WebDriverWait(driver, 10).until(
    EC.visibility_of_element_located((By.CSS_SELECTOR, 'button'))
).text

# Шаг 5: Вывод в консоль
print(f"Текст кнопки после обновления: {updated_button_text}")
assert updated_button_text == "SkyPro"

sleep(5)
driver.quit()