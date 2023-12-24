# Імпорт необхідних бібліотек
import sys
import requests
from bs4 import BeautifulSoup
import argparse

# Визначення URL для вилучення інформації
url = ""

permissions = ""

def show_help():
    print("Usage: python script.py [options]")
    print("Options:")
    print(" -u      |--url        Set url ")
    print(" -p      |--permissions        Set permissions ")
    sys.exit(0)

def parse_args():
    parser = argparse.ArgumentParser(description="Your script description.")
    parser.add_argument("-u", "--url",  help="Set url")
    parser.add_argument("-p", "--permissions",  help="Set file extension")
    return parser.parse_args()

def main():
    args = parse_args()

    if not args.permissions:
        show_help()

    
    global url
    global permissions
    
    url = args.url
    permissions = args.permissions

    try:
        # Відправлення HTTP-запиту GET на вказаний URL
        response = requests.get(url)
        
        # Перевірка на наявність помилок у HTTP-запиті
        response.raise_for_status()

        # Розбір HTML-вмісту сторінки за допомогою BeautifulSoup
        soup = BeautifulSoup(response.text, 'html.parser')

        # Вивід відформатованого HTML-вмісту (для налагодження)
        print(soup.prettify())

        # Збереження HTML-вмісту у змінну
        html_content = soup

        # Визначення шляху файлу для збереження HTML-вмісту
        file_path = f"example.{permissions}"


        # Відкриття файлу у режимі запису та запис HTML-вмісту у файл
        with open(file_path, "w", encoding="utf-8") as file:
            file.write(str(html_content))

        # Вивід повідомлення про успішне створення файлу
        print(f"Файл {file_path} успішно створено.")

    except requests.exceptions.RequestException as e:
        # Вивід повідомлення про помилку у випадку проблеми із HTTP-запитом
        print(f"Виникла помилка під час запиту: {e}")

if __name__ == "__main__":
    main()
