import wait
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time


driver = webdriver.Firefox()
driver.get('https://info.cinerama.uz/ru')

wait = WebDriverWait(driver,5)
button = wait.until(EC.element_to_be_clickable((By.XPATH, "(//button[contains(@class, 'PromoCodeModal') and @title='Promocode'])[1]")))
button.click()

# driver.quit()