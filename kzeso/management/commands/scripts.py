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
with open(f'{BASE_DIR}/kzeso/templates/contacts.html') as fp:
    soup = BeautifulSoup(fp, "html.parser")


links = []
for link in soup.find_all('script'):
    src = link.get('src')
    if src:

        script_path = src.replace('https://kzeso.com/', '').replace('//kzeso.com/', '')
        new_src = "{% static " + f" '{ script_path }' " + " %}"
        print(script_path)

        links.append(src)
        link['src'] = new_src


# #  /// SAVING SCRIPTS
for link in links:

    script_path = link.replace('https://kzeso.com/', '').replace('//kzeso.com/', '')
    save_path = f"{BASE_DIR}/kzeso/static/{ script_path }"

    print(save_path)

    # image_path =  image_url.replace('https://kzeso.com/', '')
    # list_path = image_path.split('/')
    # file_name = list_path.pop(-1)

    # new_src = "{% static " + f" '{ image_path }' " + " %}"

    # 

    # print(new_src)

    # Создание директории, если она не существует
    if not os.path.exists(os.path.dirname(save_path)):
        try:
            os.makedirs(os.path.dirname(save_path))
        except OSError:
            raise

    # # Скачивание файла
    response = requests.get(link)
    with open(save_path, 'wb') as f:
        f.write(response.content)


# # SAVING UPDATED DOCUMENT
# # Сохраняем измененный HTML документ
with open(f'{ BASE_DIR }/kzeso/templates/contacts.html', "w") as fp:
    fp.write(str(soup))