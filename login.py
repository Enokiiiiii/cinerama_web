import pytest
import selenium
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


def test_login(driver):
    wait = WebDriverWait(driver, 5)
    enter = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[contains(@class, 'Button_lg') and contains(@class, 'Button_secondary__KquHi')]")))
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