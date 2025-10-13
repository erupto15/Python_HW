from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Инициализация драйвера (укажите путь к вашему веб-драйверу)
driver = webdriver.Chrome(executable_path='path/to/chromedriver')

# Переход на сайт
driver.get('https://bonigarcia.dev/selenium-webdriver-java/loading-images.html')

# Ожидание загрузки всех изображений
wait = WebDriverWait(driver, 10)
images = wait.until(EC.presence_of_all_elements_located((By.TAG_NAME, 'img')))

# Получение значения атрибута src у третьей картинки
if len(images) >= 3:
    src_value = images[2].get_attribute('src')
    print(src_value)
else:
    print("На странице меньше трех изображений.")

# Закрытие драйвера
driver.quit()
