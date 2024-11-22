import pytest
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import time
import wait

# test profile_dropdownmenu.py

@pytest.fixture
def driver():

    driver = webdriver.Firefox()
    driver.get("https://info.cinerama.uz/ru")
    wait = WebDriverWait(driver, 5)

    try:
        # Предусловия: вход в систему
        enter = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[text()='Войти']")))
        enter.click()
        login_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[text()='C помощью логина']")))
        login_button.click()

        login = wait.until(EC.presence_of_element_located((By.ID, 'username')))
        login.click()
        login.send_keys('konstantin_bro')

        password = wait.until(EC.presence_of_element_located((By.ID, 'password')))
        password.click()
        password.send_keys('full_name')

        enter_button = wait.until(EC.element_to_be_clickable((By.XPATH, '//button[text()="Продолжить"]')))
        enter_button.click()
        time.sleep(5)

        menu = wait.until(EC.element_to_be_clickable((By.XPATH, "//*[contains(@class, 'DropdownLabel_dropdownLabel__') and @title='User-dropdown']")))
        menu.click()

        yield driver

    finally:
        try:
            menu = wait.until(EC.element_to_be_clickable((By.XPATH, "//*[contains(@class, 'DropdownLabel_dropdownLabel__') and @title='User-dropdown']")))
            menu.click()
            account = wait.until(EC.element_to_be_clickable((By.XPATH, "//*[contains(@class, 'UserDropdownMenu_dropdownItem__') and contains(@href, 'user-profile/account')]")))
            account.click()
            logout = wait.until(EC.element_to_be_clickable((By.XPATH, "//*[contains(@class, 'ListElement_listElement__') and contains(@class, 'ProfileNav_terminateButton__')]")))
            logout.click()
            confirm = wait.until(EC.element_to_be_clickable((By.XPATH, "//*[contains(@class, 'Button_secondary-red__') and contains(@class, 'Button_lg__')]")))
            confirm.click()
        except Exception as e:
            print(f"Ошибка при выходе: {e}")
        finally:
            time.sleep(2)
            driver.quit()

def test_account(driver):
    wait = WebDriverWait(driver,90)
    account = wait.until(EC.element_to_be_clickable((By.XPATH, "//*[contains(@class, 'UserDropdownMenu_dropdownItem__') and contains(@href, 'user-profile/account')]")))
    account.click()
    try:
        time.sleep(2)
        wait.until(EC.presence_of_element_located((By.XPATH, "//*[contains(@class, 'UserProfileBody_userProfileBody__IOsoi')]")))
        print('Account button passed')
    except:
        print("Account button failed")

def test_subscribe(driver):
    wait = WebDriverWait(driver,90)
    subscribe = wait.until(EC.element_to_be_clickable((By.XPATH, "//*[contains(@class, 'UserDropdownMenu_dropdownItem__') and contains(@href, '/user-profile/subscriptions')]")))
    subscribe.click()
    try:
        time.sleep(2)
        wait.until(EC.presence_of_element_located((By.XPATH, "//*[contains(@class, 'Tabs_tabs__') and contains(@class, 'UserSubscriptionsView_profileContent__')]")))
        print('subscribe passed')
    except:
        print('subscribe failed')

def test_favorite(driver):
    wait = WebDriverWait(driver, 5)
    favorite = wait.until(EC.element_to_be_clickable((By.XPATH, "(//a[contains(@href, '/user-profile/favorites')])[1]")))
    favorite.click()
    try:
        time.sleep(2)
        wait.until(EC.presence_of_element_located((By.XPATH, "//*[contains(@class, 'MovieList_topPanel__')]")))
        print('favorite passed')
    except:
        print('favorite failed')

def test_history(driver):
    wait = WebDriverWait(driver, 5)
    history = wait.until(EC.element_to_be_clickable((By.XPATH, "//a[contains(@href, '/user-profile/history') and contains(@class, 'UserDropdownMenu_dropdownItem__')]")))
    history.click()
    try:
        time.sleep(2)
        wait.until(EC.presence_of_element_located((By.XPATH, "//h2[contains(@class, 'SectionHeading_sectionHeading__') and contains(@class, 'SectionHeading_gradient__')]")))
        print('history passed')
    except:
        print('history failed')

def test_user_help(driver):
    wait = WebDriverWait(driver, 5)
    user_help = wait.until(EC.element_to_be_clickable((By.XPATH, "//a[contains(@href, '/user-profile/help') and contains(@class, 'UserDropdownMenu_dropdownItem__')]")))
    user_help.click()
    try:
        time.sleep(2)
        wait.until(EC.presence_of_element_located((By.XPATH, "//div[contains(@class, 'UserProfileBody_userProfileBody__') and contains(@class, 'UserHelpView_profileWrapper__')]")))
        print('user_help passed')
    except:
        print('user_help failed')