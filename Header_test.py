import pytest
import wait
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import time
from selenium.common.exceptions import UnexpectedAlertPresentException, NoAlertPresentException
from selenium.common.exceptions import TimeoutException

@pytest.fixture
def driver():
    driver = webdriver.Firefox()
    driver.get("https://info.cinerama.uz/ru")
    time.sleep(5)
    yield driver
    driver.quit()


wait = WebDriverWait(driver,2)

#log
log_file = "check_log.txt"
#press genre-button
def test_genre(driver):
    wait = WebDriverWait(driver, 5)
    genre_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[contains(@class, 'IconButton_iconButtonBase__') and contains(@class, 'CategoryPanel_categoryButton__') and @type='button']")))
    genre_button.click()
    try:
        wait.until(EC.presence_of_element_located((By.XPATH, "(//h2[contains(@class, 'SectionHeading_gradient__') and contains(@class, 'SectionHeading_sectionHeading__')])[1]")))
        print('genre-button Passed')
        genre_button.click()
    except:
        print('genre-button Failed')
        genre_button.click()

#press button-TV
def test_TV(driver):
    wait = WebDriverWait(driver, 5)
    TV_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//a[contains(@href, '/online-tv?category')]")))
    TV_button.click()
    try:
        wait = WebDriverWait(driver, 5)
        wait.until(EC.presence_of_element_located((By.XPATH, "//div[contains(@class, 'OnlineTvList_wrapper__')]")))
        print("button-TV passed")
    except:
        print('button-TV failed')

#press button-subscribes
def test_subscriptions(driver):
    wait = WebDriverWait(driver, 5)
    subscribe_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//a[@href='/ru/subscriptions']")))
    subscribe_button.click()
    try:
        wait.until(EC.presence_of_element_located((By.CLASS_NAME, 'SubscriptionMainCard_subscriptionMainCard__8QN3J')))
        print("button-subscribes passed")
    except:
        print("button-subscribes failed")

# promocode
def test_promocode(driver):
    wait = WebDriverWait(driver,5)
    promocode = wait.until(EC.element_to_be_clickable((By.XPATH, "(//button[contains(@class, 'PromoCodeModal') and @title='Promocode'])[1]")))
    promocode.click()
    try:
        wait.until(EC.presence_of_element_located((By.CLASS_NAME, 'Modal_modal__l4yBn')))
        print('promocode passed')
        title = "Закрыть"
        close = WebDriverWait(driver, 2).until(EC.element_to_be_clickable((By.XPATH, f"//button[@title='{title}']")))
        close.click()
    except:
        print('promocode failed')

# press notification-button
def test_notification(driver):
    wait = WebDriverWait(driver, 5)
    notification_button = wait.until(EC.element_to_be_clickable((By.CLASS_NAME, 'SecondaryNav_notificationsIcon__2zJQu')))
    notification_button.click()
    try:
        wait.until(EC.presence_of_element_located((By.CLASS_NAME, 'NotificationView_container__WyvxJ')))
        print('notification_button passed')
    except:
        print('notification_button false')

# press language-choise
def test_change_lang(driver):
    wait = WebDriverWait(driver, 5)
    language = wait.until(EC.element_to_be_clickable((By.CLASS_NAME, 'LanguageDropdown_labelIcon__wplgV')))
    language.click()
    try:
        wait.until(EC.presence_of_element_located((By.CLASS_NAME,'DropdownMenu_dropdown__wGZDL')))
        print('language list passed')
    except:
        print('language button failed')

# press Event-button
def test_discount(driver):
    wait = WebDriverWait(driver, 5)
    discount_button = wait.until(EC.element_to_be_clickable((By.CLASS_NAME, 'Button_md__zUJhY')))
    discount_button.click()
    try:
        wait.until(EC.presence_of_element_located((By.CLASS_NAME, 'SubscriptionMainCard_subscriptionMainCard__8QN3J')))
        print('event_button passed')
    except:
        print('event_button failed')

# press Log-in button
def test_log_in(driver):
    wait = WebDriverWait(driver, 3)
    log_in = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[contains(@class, 'Button_lg') and contains(@class, 'Button_secondary__KquHi')]")))
    log_in.click()
    try:
        wait.until(EC.presence_of_element_located((By.CLASS_NAME, 'AuthVerificationTabs_authVerificationTabs__ihDUO')))
        print('log_in button passed')
        title = "Закрыть"
        close = WebDriverWait(driver,2).until(EC.element_to_be_clickable((By.XPATH, f"//button[@title='{title}']")))
        close.click()
    except:
        print('log_in button failed')
# search
def test_search(driver):
    wait = WebDriverWait(driver,3)
    time.sleep(5)
    search = wait.until(EC.presence_of_element_located((By.ID, 'search')))
    time.sleep(5)
    search.click()
    search.send_keys('пират')
    try:
        time.sleep(5)
        wait.until(EC.presence_of_element_located((By.CLASS_NAME, 'SearchResultsButton_searchResultsButton__hN3w5')))
        print("search passed")
        close = WebDriverWait(driver, 2).until(EC.element_to_be_clickable((By.CLASS_NAME,"SearchForm_toggler___Svqt")))
        close.click()
    except:
        print('search failed')

def test_my_and_login(driver):
    wait = WebDriverWait(driver, 5)
    enter = wait.until(EC.element_to_be_clickable(
        (By.XPATH, "//button[contains(@class, 'Button_lg') and contains(@class, 'Button_secondary__')]")))
    enter.click()
    wait = WebDriverWait(driver, 2)
    login_button = wait.until(EC.element_to_be_clickable(
        (By.XPATH, "(//*[contains(@class, 'AuthVerificationTabs_authVerificationTab__')])[2]")))
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
    time.sleep(5)
    wait = WebDriverWait(driver,5)
    My_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//a[contains(@class, 'PrimaryNav_navLink__') and @title='Favorites']")))
    My_button.click()
    try:
        wait = WebDriverWait(driver,10)
        wait.until(EC.presence_of_element_located((By.XPATH, "//a[contains(@href, '/users-history/history')]")))
        print('My_button passed')
    except:
        print("My_button failed")

#press home-button
def test_home(driver):
    wait = WebDriverWait(driver,5)
    home_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//*[contains(@class, 'Logo_logoIcon__')]")))
    home_button.click()
    try:
        wait = WebDriverWait(driver,3)
        wait.until(EC.presence_of_element_located((By.XPATH, "//*[contains(@class, 'BannerSlider_bannerSliderWrapper__')]")))
        print("home_button passed")
    except:
        print("home_button failed")