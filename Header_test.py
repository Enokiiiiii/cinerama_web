import sys
import os
sys.path.insert(0, os.path.abspath(os.path.dirname(__file__)))
from precondition import driver_web
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import time

def test_genre(driver_web):
    wait = WebDriverWait(driver_web, 10)
    genre_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[contains(@class, 'IconButton_iconButtonBase__') and contains(@class, 'CategoryPanel_categoryButton__')]")))
    genre_button.click()
    try:
        wait.until(EC.presence_of_element_located((By.XPATH, "(//*[contains(@class, 'SectionHeading_gradient__') and contains(@class, 'SectionHeading_sectionHeading__')])[1]")))
        print('genre-button Passed')
        genre_button.click()
    except:
        print('genre-button Failed')
        genre_button.click()

#press button-TV
def test_TV(driver_web):
    wait = WebDriverWait(driver_web, 10)
    TV_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//a[contains(@href, '/online-tv?category')]")))
    TV_button.click()
    try:
        wait.until(EC.presence_of_element_located((By.XPATH, "//div[contains(@class, 'OnlineTvList_wrapper__')]")))
        print("button-TV passed")
    except:
        print('button-TV failed')

#press button-subscribes
def test_subscriptions(driver_web):
    wait = WebDriverWait(driver_web, 10)
    subscribe_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//a[contains(@href, '/subscriptions')]")))
    subscribe_button.click()
    try:
        wait.until(EC.presence_of_element_located((By.XPATH, "//div[contains(@class, 'SubscriptionMainCard_subscriptionMainCard__')]")))
        print("button-subscribes passed")
    except:
        print("button-subscribes failed")

# promocode
def test_promocode(driver_web):
    wait = WebDriverWait(driver_web,10)
    promocode = wait.until(EC.element_to_be_clickable((By.XPATH, "(//button[contains(@class, 'PromoCodeModal') and @title='Promocode'])[1]")))
    promocode.click()
    try:
        wait.until(EC.presence_of_element_located((By.XPATH, "//input[contains (@class, 'FormInput_formInput__9mRtl') and @id = 'code']")))
        print('promocode passed')
        close = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[contains(@class, 'Button_button__9kCH4') and contains(@class, 'Modal_modalCloseButton__')]")))
        close.click()
        time.sleep(1)
    except:
        print('promocode failed')

# notification-button
# def test_notification(driver):
#     wait = WebDriverWait(driver, 10)
#     notification_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//a[contains(@class, 'SecondaryNav_notificationsIcon__') and @title = 'Notifications']")))
#     notification_button.click()
#     try:
#         wait.until(EC.presence_of_element_located((By.CLASS_NAME, 'NotificationView_container__WyvxJ')))
#         print('notification_button passed')
#     except:
#         print('notification_button false')

# press language-choise
def test_change_lang(driver_web):
    wait = WebDriverWait(driver_web, 10)
    language = wait.until(EC.element_to_be_clickable((By.XPATH, "//*[contains(@class, 'DropdownLabel_dropdownLabel__') and @title='Language-dropdown']")))
    language.click()
    try:
        wait.until(EC.presence_of_element_located((By.XPATH,"//div[contains(@class, 'DropdownMenu_dropdown__') and contains(@class, 'DropdownMenu_bottom-left__')]")))
        print('language list passed')
        language.click()
    except:
        print('language button failed')
        language.click()

# search
def test_search(driver_web):
    wait = WebDriverWait(driver_web, 10)
    search = wait.until(EC.element_to_be_clickable((By.ID, 'search')))
    search.click()
    search.send_keys('пират')
    try:
        wait.until(EC.presence_of_element_located((By.XPATH, "//a[contains(@class, 'SearchResultsButton_searchResultsButton__')]")))
        print("search passed")
        close_o = wait.until(EC.presence_of_element_located((By.XPATH, "//button[contains(@class, 'SearchForm_toggler___') and contains(@class, 'IconButton_iconButtonBase__')]")))
        close_o.click()
    except:
        print('search failed')

def test_my(driver_web):
    wait = WebDriverWait(driver_web, 10)
    my_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//a[contains(@class, 'PrimaryNav_navLink__') and @title='Favorites']")))
    my_button.click()
    try:
        wait.until(EC.presence_of_element_located((By.XPATH, "//a[contains(@href, '/users-history/history')]")))
        print('My_button passed')
    except:
        print("My_button failed")

#press home-button
def test_home(driver_web):
    wait = WebDriverWait(driver_web,10)
    home_button = wait.until(EC.element_to_be_clickable((By.XPATH, "(//*[contains(@class, 'Logo_logoIcon__')])[1]")))
    home_button.click()
    try:
        wait.until(EC.presence_of_element_located((By.XPATH, "//*[contains(@class, 'BannerSlider_bannerSliderWrapper__')]")))
        print("home_button passed")
    except:
        print("home_button failed")