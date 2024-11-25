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
driver.get('https://info.cinerama.uz/ru')

# Authorisation
def test_Autorisation():
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
    time.sleep(2)

#open profile page
def test_Open_profilepage():
    menu = WebDriverWait(driver,2).until(EC.element_to_be_clickable((By.CLASS_NAME, 'UserDropdownMenu_profileDropdown__myoDy')))
    menu.click()
    time.sleep(1)

    account = wait.until(EC.element_to_be_clickable((By.XPATH, "//a[@href='/ru/user-profile/account']")))
    account.click()
    wait.until(EC.presence_of_element_located((By.CLASS_NAME, 'ProfileNav_listWrapper__IQ2AC')))
    time.sleep(2)

#test menu
def test_menu():
    device = wait.until(EC.element_to_be_clickable((By.XPATH, "//a[@href='/ru/user-profile/sessions']")))
    device.click()
    try:
        time.sleep(2)
        wait.until(EC.presence_of_element_located((By.CLASS_NAME, 'UserSessionsView_titleWrapper__VcDBd')))
        print('device passed')
    except:
        print('device failed')


exit_button = wait.until(EC.element_to_be_clickable((By.CLASS_NAME, 'UserSessionTerminate_terminateButton__FI5h7')))
exit_button.click()
try:
    time.sleep(2)
    wait.until(EC.presence_of_element_located((By.CLASS_NAME, 'Alert_alertModal__vZqJz')))
    print('exit_button passed')
except:
    print('exit_button failed')
close = wait.until(EC.element_to_be_clickable((By.CLASS_NAME, 'Modal_modalCloseButton__qzUyx')))
close.click()

cards = wait.until(EC.element_to_be_clickable((By.XPATH, "//a[@href='/ru/user-profile/payments']")))
cards.click()
try:
    time.sleep(2)
    wait.until(EC.presence_of_element_located((By.CLASS_NAME, 'UserBalanceRow_userBalanceWrapper__TzQXM')))
    print('cards passed')
except:
    print('cards failed')

time.sleep(2)
add_card = wait.until(EC.element_to_be_clickable((By.CLASS_NAME, 'Button_primary-gradient__BJwfV')))
add_card.click()
wait.until(EC.presence_of_element_located((By.CLASS_NAME, 'Modal_modal__l4yBn')))

card_numb = wait.until(EC.element_to_be_clickable((By.ID, 'card_number')))
card_numb.click()
card_numb.send_keys('1234123412341324')
card_valid = wait.until(EC.element_to_be_clickable((By.ID, 'card_exp')))
card_valid.click()
card_valid.send_keys('1029')


add_card_button = wait.until(EC.element_to_be_clickable((By.CLASS_NAME, 'Form_formFooter__TAqJ0')))
add_card_button.click()
try:
    time.sleep(2)
    wait.until(EC.presence_of_element_located((By.CLASS_NAME, 'Modal_modalContainer__KKr8n ')))
    print('add_card_button passed')
except:
    print('add_card_button failed')
# close browser
driver.quit()



