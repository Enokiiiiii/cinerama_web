from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.common.exceptions import StaleElementReferenceException, ElementNotInteractableException

driver = webdriver.Firefox()
driver.get("https://info.cinerama.uz/ru")

# Находим все карусели по классу или другому общему признаку
carousels = driver.find_elements(By.CLASS_NAME, 'Slider_swiperWrapper__3cT2Y')  # Предположим, что у всех каруселей один класс

# Проходим по каждой карусели и выполняем тесты
for i, carousel in enumerate(carousels):
    print(f"Тестирование карусели {i + 1}")

    # Повторяем процесс нахождения кнопок и кликов для обработки возможных StaleElementReferenceException
    while True:
        try:
            # Находим кнопки навигации внутри карусели
            next_button = carousel.find_element(By.CLASS_NAME, 'SlideNavigationButton_right__J5Upc')
            prev_button = carousel.find_element(By.CLASS_NAME, 'SlideNavigationButton_left__piQ0E')

            # Прокручиваем кнопки в область видимости перед кликом
            driver.execute_script("arguments[0].scrollIntoView(true);", next_button)
            time.sleep(0.5)  # Небольшая пауза для завершения прокрутки

            # Переход вперед
            next_button.click()
            time.sleep(1)  # Пауза для анимации

            # Прокручиваем кнопку назад в область видимости перед кликом
            driver.execute_script("arguments[0].scrollIntoView(true);", prev_button)
            time.sleep(0.5)

            # Переход назад
            prev_button.click()
            time.sleep(1)  # Пауза для анимации

            print(f"Карусель {i + 1} успешно протестирована.")
            break  # Если успешно, выходим из цикла
        except (StaleElementReferenceException, ElementNotInteractableException):
            print(f"Ошибка взаимодействия с элементом в карусели {i + 1}. Повторный поиск...")
            time.sleep(1)  # Небольшая задержка перед повторной попыткой
        except Exception as e:
            print(f"Ошибка в карусели {i + 1}: {e}")
            break

driver.quit()


##############################################################################


from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

driver = webdriver.Chrome()
driver.get("https://example.com")

# Список заголовков h2 и соответствующих элементов для ожидания
headers_to_click = {
    "Заголовок 1": {"locator": (By.ID, "element_id_1"), "url": "https://example.com/page1"},
    "Заголовок 2": {"locator": (By.CLASS_NAME, "element_class_2"), "url": "https://example.com/page2"},
    # Добавьте больше заголовков и элементов для ожидания, если необходимо
}

# Перебираем каждый заголовок h2 и его условие
for title, data in headers_to_click.items():
    try:
        # Находим заголовок h2 по тексту и кликаем по нему
        header = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, f"//h2[text()='{title}']")))
        driver.execute_script("arguments[0].scrollIntoView(true);", header)
        header.click()

        # Ждем появления уникального элемента на новой странице или в новой секции
        expected_locator = data["locator"]
        WebDriverWait(driver, 10).until(EC.presence_of_element_located(expected_locator))
        print(f"Уникальный элемент для {title} найден.")

    except TimeoutException:
        print(f"Ошибка: уникальный элемент для {title} не найден.")
    except Exception as e:
        print(f"Ошибка при клике на заголовок '{title}': {e}")

    # Возвращаемся на исходную страницу, если нужно
    driver.get("https://example.com")  # Замените URL на нужный, если требуется возврат

# Завершаем сессию
driver.quit()




