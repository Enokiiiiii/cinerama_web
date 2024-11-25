import wait
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import time
from selenium.common.exceptions import UnexpectedAlertPresentException, NoAlertPresentException
from selenium.common.exceptions import TimeoutException

driver = webdriver.Firefox()
driver.get('https://info.cinerama.uz/ru/online-tv')
wait.until(EC.presence_of_element_located((By.CLASS_NAME, 'OnlineTvListView_sectionHeading__Gx8Ol')))

wait = WebDriverWait(driver, 5)
enter = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[text()='Войти']")))
enter.click()

wait = WebDriverWait(driver, 2)
login_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[text()='C помощью логина']")))
login_button.click()

wait = WebDriverWait(driver, 3)
login = wait.until(EC.presence_of_element_located((By.ID, 'username')))
login.click()
login.send_keys('')

wait = WebDriverWait(driver, 3)
password = wait.until(EC.presence_of_element_located((By.ID, 'password')))
password.click()
password.send_keys('')

enter_button = wait.until(EC.element_to_be_clickable((By.XPATH, '//button[text()="Продолжить"]')))
enter_button.click()
try:
    categories = wait.until(EC.presence_of_element_located((By.CLASS_NAME, 'CategoriesList_categoriesList__AySi2')))
    print('Online tv page Passed')
except:
    print('Online tv page failed')

time.sleep(5)
channel_button = wait.until(EC.presence_of_element_located((By.XPATH, "//img[@alt='Первый']")))
channel_button.click()
try:
    wait.until(EC.presence_of_element_located((By.CLASS_NAME, 'OnlineTvPlayerPanel_playerPanel__qavXV')))
    time.sleep(5)
    print('ТВ работает')
    driver.back()
except:
    print("ТВ не работает")
    time.sleep(5)
    driver.back()

channel_button_2 = wait.until(EC.presence_of_element_located((By.XPATH, "//img[@alt='НТВ']")))
time.sleep(5)
channel_button_2.click()
try:
    wait.until(EC.presence_of_element_located((By.CLASS_NAME, 'VerificationModal_subscriptionModalBody__Ne2Uj')))
    time.sleep(5)
    print('платное ТВ работает')
    driver.back()
except:
    time.sleep(5)
    print("платное ТВ не работает")
    driver.back()

driver.close()
