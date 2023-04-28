from django.core.management.base import BaseCommand, CommandError
from bs4 import BeautifulSoup
import requests, os

from django.conf import settings
from django.conf.urls.static import static


BASE_DIR = settings.BASE_DIR

class Command(BaseCommand):
    args = ''
    help = ''

    def handle(self, *args, **options):
        pass

"""

# Получаем HTML-документ по указанному URL
url = 'https://example.com'
response = requests.get(url)
html_doc = response.text

# Создаем объект BeautifulSoup и находим все ссылки в документе
soup = BeautifulSoup(html_doc, 'html.parser')
links = []
for link in soup.find_all('a'):
    href = link.get('href')
    if href:
        links.append(href)

# Выводим список ссылок
print(links)

"""

# print(BASE_DIR)

# Получаем HTML-документ по указанному URL
# url = 'https://kzeso.com/'
# response = requests.get(url)
# html_doc = response.text

# print(html_doc)


# with open(f'{BASE_DIR}/kzeso/templates/index.html', 'r') as file:
#     html_doc = file.read()
#     print(html_doc)

# SEARCH LINKS IN DOCUMENT
with open(f'{BASE_DIR}/kzeso/templates/contacts-source.html') as fp:
    soup = BeautifulSoup(fp, "html.parser")


links = []
for link in soup.find_all('link'):
    href = link.get('href')
    if href:

        css = True if '.css' in href else False
        png = True if '.png' in href else False

        if css or png:
            # print(f'{ href }')

            script_path = href.replace('https://kzeso.com/', '').replace('//kzeso.com/', '')
            static_value = "{% static " + f"'{ script_path }'" + " %}"

            links.append(href)
            print(static_value)
            link['href'] = static_value

print("\n=================================================\n")

# #  /// SAVING SCRIPTS
for link in links:

    script_path = link.replace('https://kzeso.com/', '').replace('//kzeso.com/', '')
    save_path = f"{BASE_DIR}/kzeso/static/{ script_path }"

    print(
        f"From: { link }\nTo: {save_path}\n\n",

    )

    # Создание директории, если она не существует
    if not os.path.exists(os.path.dirname(save_path)):
        try:
            os.makedirs(os.path.dirname(save_path))
        except OSError:
            raise

    # Скачивание файла
    response = requests.get(link)
    with open(save_path, 'wb') as f:
        f.write(response.content)


# # Сохраняем измененный HTML документ
with open(f'{ BASE_DIR }/kzeso/templates/contacts.html', "w") as fp:
    fp.write(str(soup))