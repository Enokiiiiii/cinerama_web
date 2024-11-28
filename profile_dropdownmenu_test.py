import time

import pytest
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from precondition import driver_web
from precondition import dropdown_button


def test_account(driver_web, dropdown_button):
    wait = WebDriverWait(driver_web,10)
    account = wait.until(EC.element_to_be_clickable((By.XPATH, "//*[contains(@class, 'UserDropdownMenu_dropdownItem__') and contains(@href, '/user-profile/account')]")))
    account.click()
    try:
        wait = WebDriverWait(driver_web, 10)
        wait.until(EC.presence_of_element_located((By.XPATH, "//*[contains(@class, 'UserProfileBody_userProfileBody__IOsoi')]")))
        print('Account button passed')
    except:
        print("Account button failed")

def test_subscribe(driver_web, dropdown_button):
    wait = WebDriverWait(driver_web,10)
    subscribe = wait.until(EC.element_to_be_clickable((By.XPATH, "//*[contains(@class, 'UserDropdownMenu_dropdownItem__') and contains(@href, '/user-profile/subscriptions')]")))
    subscribe.click()
    try:
        wait = WebDriverWait(driver_web, 10)
        wait.until(EC.presence_of_element_located((By.XPATH, "//*[contains(@class, 'Tabs_tabs__') and contains(@class, 'UserSubscriptionsView_profileContent__')]")))
        print('subscribe passed')
    except:
        print('subscribe failed')

def test_favorite(driver_web, dropdown_button):
    wait = WebDriverWait(driver_web, 10)
    favorite = wait.until(EC.element_to_be_clickable((By.XPATH, "(//a[contains(@href, '/user-profile/favorites')])[1]")))
    favorite.click()
    try:
        wait = WebDriverWait(driver_web, 10)
        wait.until(EC.presence_of_element_located((By.XPATH, "//*[contains(@class, 'MovieList_topPanel__')]")))
        print('favorite passed')
    except:
        print('favorite failed')

def test_history(driver_web, dropdown_button):
    wait = WebDriverWait(driver_web, 10)
    history = wait.until(EC.element_to_be_clickable((By.XPATH, "//a[contains(@href, '/user-profile/history') and contains(@class, 'UserDropdownMenu_dropdownItem__')]")))
    history.click()
    try:
        wait = WebDriverWait(driver_web, 10)
        wait.until(EC.presence_of_element_located((By.XPATH, "//h2[contains(@class, 'SectionHeading_sectionHeading__') and contains(@class, 'SectionHeading_gradient__')]")))
        print('history passed')
    except:
        print('history failed')

def test_user_help(driver_web, dropdown_button):
    wait = WebDriverWait(driver_web, 10)
    user_help = wait.until(EC.element_to_be_clickable((By.XPATH, "//a[contains(@href, '/user-profile/help') and contains(@class, 'UserDropdownMenu_dropdownItem__')]")))
    user_help.click()
    try:
        wait = WebDriverWait(driver_web, 10)
        wait.until(EC.presence_of_element_located((By.XPATH, "//div[contains(@class, 'UserProfileBody_userProfileBody__') and contains(@class, 'UserHelpView_profileWrapper__')]")))
        print('user_help passed')
    except:
        print('user_help failed')