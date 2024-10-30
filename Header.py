
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

wait = WebDriverWait(driver,2)

#log
log_file = "check_log.txt"

wait.until(EC.presence_of_element_located((By.CLASS_NAME,'BannerSlider_bannerSliderWrapper__AtFAy')))


#press home-button
home_button = wait.until(EC.element_to_be_clickable((By.CLASS_NAME, "Logo_logoBase__o4no_")))
home_button.click()

#press genre-button
genre_button = wait.until(EC.element_to_be_clickable((By.CLASS_NAME, 'IconButton_iconButtonBase__ixeDa')))
genre_button.click()
try:
    serials_element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, 'Image_imageWrapper__m8qmz')))
    print('genre-button Passed')
except:
    print('genre-button Failed')
genre_button.click()

#press button-TV
TV_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//a[@href='/ru/online-tv']")))
TV_button.click()
try:
    online_tv_genre = wait.until(EC.presence_of_element_located((By.ID, '3')))
    print("button-TV passed")
except:
    print('button-TV failed')

#press button-subscribes
subscribe_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//a[@href='/ru/subscriptions']")))
subscribe_button.click()
try:
    wait.until(EC.presence_of_element_located((By.CLASS_NAME, 'SubscriptionMainCard_subscriptionMainCard__8QN3J')))
    print("button-subscribes passed")
except:
    print("button-subscribes failed")

promocode = wait.until(EC.element_to_be_clickable((By.CLASS_NAME, 'PromoCodeModal_navLink__l6zRY')))
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
notification_button = wait.until(EC.element_to_be_clickable((By.CLASS_NAME, 'SecondaryNav_notificationsIcon__2zJQu')))
notification_button.click()
try:
    wait.until(EC.presence_of_element_located((By.CLASS_NAME, 'NotificationView_container__WyvxJ')))
    print('notification_button passed')
except:
    print('notification_button false')

# press language-choise
language = wait.until(EC.element_to_be_clickable((By.CLASS_NAME, 'LanguageDropdown_labelIcon__wplgV')))
language.click()
try:
    wait.until(EC.presence_of_element_located((By.CLASS_NAME,'DropdownMenu_dropdown__wGZDL')))
    print('language list passed')
except:
    print('language button failed')

# press Event-button
event_button = wait.until(EC.element_to_be_clickable((By.CLASS_NAME, 'Button_md__zUJhY')))
event_button.click()
try:
    wait.until(EC.presence_of_element_located((By.CLASS_NAME, 'SubscriptionMainCard_subscriptionMainCard__8QN3J')))
    print('event_button passed')
except:
    print('event_button failed')

# press Log-in button
wait = WebDriverWait(driver, 3)
log_in = wait.until(EC.element_to_be_clickable((By.CLASS_NAME, 'Button_secondary__KquHi')))
log_in.click()
try:
    wait.until(EC.presence_of_element_located((By.CLASS_NAME, 'AuthVerificationTabs_authVerificationTabs__ihDUO')))
    print('log_in button passed')
    title = "Закрыть"
    close = WebDriverWait(driver,2).until(EC.element_to_be_clickable((By.XPATH, f"//button[@title='{title}']")))
    close.click()
except:
    print('log_in button failed')

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


time.sleep(3)
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

time.sleep(5)
My_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//a[@href='/ru/users-history/favorites']")))
My_button.click()
try:
    time.sleep(3)
    wait.until(EC.presence_of_element_located((By.CLASS_NAME, 'SectionHeading_sectionHeading__H_1Yh')))
    wait.until(EC.presence_of_element_located((By.XPATH, "//a[@href='/ru/users-history/history']")))
    print('My_button passed')
except:
    print("My_button failed")

# close browser
driver.quit()