import wait
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import pytest


from precondition import driver
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