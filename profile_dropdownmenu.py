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
driver.get("https://info.cinerama.uz/ru")

wait = WebDriverWait(driver, 10)

wait = WebDriverWait(driver, 5)
enter = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[text()='Войти']")))
enter.click()

wait = WebDriverWait(driver, 2)
login_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[text()='C помощью логина']")))
login_button.click()

wait = WebDriverWait(driver, 3)
login = wait.until(EC.presence_of_element_located((By.ID, 'username')))
login.click()
login.send_keys('konstantin_bro')

wait = WebDriverWait(driver, 3)
password = wait.until(EC.presence_of_element_located((By.ID, 'password')))
password.click()
password.send_keys('full_name')

enter_button = wait.until(EC.element_to_be_clickable((By.XPATH, '//button[text()="Продолжить"]')))
enter_button.click()
time.sleep(2)

menu = WebDriverWait(driver,2).until(EC.element_to_be_clickable((By.CLASS_NAME, 'UserDropdownMenu_profileDropdown__myoDy')))
menu.click()
time.sleep(1)

account = wait.until(EC.element_to_be_clickable((By.XPATH, "//a[@href='/ru/user-profile/account']")))
account.click()
try:
    time.sleep(2)
    wait.until(EC.presence_of_element_located((By.CLASS_NAME, 'UserProfileBody_userProfileBody__IOsoi')))
    print('Account button passed')
except:
    print("Account button failed")

menu.click()
subscribe = wait.until(EC.element_to_be_clickable((By.XPATH, "//*[text()='Подписки и тарифы']")))
subscribe.click()
try:
    time.sleep(2)
    wait.until(EC.presence_of_element_located((By.XPATH, "//img[@alt='primary-placeholder-image']")))
    print('subscribe passed')
except:
    print('subscribe failed')

# close browser
driver.quit()