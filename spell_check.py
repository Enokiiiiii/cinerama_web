import wait
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import time
from selenium.common.exceptions import UnexpectedAlertPresentException, NoAlertPresentException
from selenium.common.exceptions import TimeoutException

# Установка драйвера Selenium
driver = webdriver.Firefox()

# Список для хранения уникальных ссылок
visited_links = set()


# Функция для проверки орфографии с помощью LanguageTool
def check_spelling(text):
    url = "https://api.languagetoolplus.com/v2/check"
    data = {
        'text': text,
        'language': 'ru'  # Укажите нужный язык
    }
    response = requests.post(url, data=data)
    result = response.json()
    return result['matches']


# Функция для сбора ссылок на странице
def get_all_links(url):
    driver.get(url)
    soup = BeautifulSoup(driver.page_source, "html.parser")
    links = [a.get('href') for a in soup.find_all('a', href=True)]
    # Преобразование относительных ссылок в абсолютные и фильтрация внешних ссылок
    links = [link if link.startswith('http') else f"{url.rstrip('/')}/{link.lstrip('/')}" for link in links]
    return set(links)


# Основная функция проверки сайта
def check_website(url):
    links_to_visit = get_all_links(url)

    while links_to_visit:
        link = links_to_visit.pop()

        # Пропускаем уже посещенные ссылки
        if link in visited_links:
            continue
        visited_links.add(link)

        # Загружаем страницу
        driver.get(link)
        time.sleep(1)  # Пауза для загрузки страницы (опционально, чтобы избежать блокировки)

        # Извлечение текста всей страницы
        soup = BeautifulSoup(driver.page_source, "html.parser")
        page_text = soup.get_text()

        # Проверка орфографии
        errors = check_spelling(page_text)

        # Вывод ошибок
        if errors:
            print(f"\nНа странице {link} найдены ошибки:")
            for error in errors:
                print("Ошибка:", error['message'])
                print("Текст с ошибкой:", error['context']['text'])
                print("Предложения для исправлений:", [suggestion['value'] for suggestion in error['replacements']])
        else:
            print(f"На странице {link} ошибок не найдено.")

        # Собираем ссылки на новые страницы
        new_links = get_all_links(link)
        links_to_visit.update(new_links - visited_links)


# Запуск проверки сайта
check_website("https://info.cinerama.uz/ru")

# Закрытие драйвера
driver.quit()
 # добавить исключения
