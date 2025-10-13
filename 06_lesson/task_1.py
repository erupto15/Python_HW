from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

driver = webdriver.Chrome()

#Шаг 1. Переходим на страницу сайта
driver.get('http://uitestingplayground.com/ajax')

#Шаг 2. Нажать на синюю кнопку
button = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.CSS_SELECTOR, 'button'))
)
button.click()

#Шаг 3. Получение текста из зеленой кнопки
massage = WebDriverWait(driver, 10).until(
    EC.visibility_of_element_located((By.CSS_SELECTOR, '.alert'))
)
text = massage.text

#Шаг 4. Вывод в консоль
print(f"Полученный текст:{text}")
assert text == "Data loaded with AJAX get request."

time.sleep(5)
driver.quit()

