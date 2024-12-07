from precondition import driver_web
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium import webdriver

driver = webdriver.Firefox()
driver.get("https://info.cinerama.uz/ru")
WebDriverWait(driver, 10).until(EC.alert_is_present())
pas_alert = driver.switch_to.alert
pas_alert.send_keys("good-job")
pas_alert.accept()
wait = WebDriverWait(driver, 10)
try:
    enter = wait.until(
        EC.element_to_be_clickable(
            (
                By.XPATH,
                "//button[contains(@class, 'Button_lg__') and contains(@class, 'Button_secondary__')]",
            )
        )
    )
    enter.click()
    login_button = wait.until(
        EC.element_to_be_clickable(
            (
                By.XPATH,
                "(//button[contains(@class, 'AuthVerificationTabs_authVerificationTab__')])[2]",
            )
        )
    )
    login_button.click()

    login = wait.until(EC.presence_of_element_located((By.ID, "username")))
    login.click()
    login.send_keys("konstantin_bro")

    password = wait.until(EC.presence_of_element_located((By.ID, "password")))
    password.click()
    password.send_keys("full_name")

    enter_button = wait.until(
        EC.element_to_be_clickable(
            (
                By.XPATH,
                "//button[contains(@class, 'Button_primary__') and @type='submit']",
            )
        )
    )
    enter_button.click()

    wait.until(
        EC.presence_of_element_located(
            (
                By.XPATH,
                "//*[contains(@class, 'BannerSlider_bannerSliderWrapper__')]",
            )
        )
    )
    yield driver

finally:
    try:
        menu = wait.until(
            EC.element_to_be_clickable(
                (
                    By.XPATH,
                    "//*[contains(@class, 'DropdownLabel_dropdownLabel__') and @title='User-dropdown']",
                )
            )
        )
        menu.click()
        account = wait.until(
            EC.element_to_be_clickable(
                (
                    By.XPATH,
                    "//*[contains(@class, 'UserDropdownMenu_dropdownItem__') and contains(@href, 'user-profile/account')]",
                )
            )
        )
        account.click()
        logout = wait.until(
            EC.element_to_be_clickable(
                (
                    By.XPATH,
                    "//*[contains(@class, 'ListElement_listElement__') and contains(@class, 'ProfileNav_terminateButton__')]",
                )
            )
        )
        logout.click()
        confirm = wait.until(
            EC.element_to_be_clickable(
                (
                    By.XPATH,
                    "//*[contains(@class, 'Button_secondary-red__') and contains(@class, 'Button_lg__')]",
                )
            )
        )
        confirm.click()
    except Exception as e:
        print(f"Ошибка при выходе: {e}")
    finally:
        wait.until(
            EC.presence_of_element_located(
                (
                    By.XPATH,
                    "//button[contains(@class, 'Button_lg__') and contains(@class, 'Button_secondary__')]",
                )
            )
        )
        driver.quit()
