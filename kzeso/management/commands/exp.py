import re
import requests
from django.core.management.base import BaseCommand, CommandError
from bs4 import BeautifulSoup
import requests, os
from time import sleep

from django.conf import settings
from django.conf.urls.static import static


BASE_DIR = settings.BASE_DIR

class Command(BaseCommand):
    args = ''
    help = ''

    def handle(self, *args, **options):
        pass



# Загружаем HTML документ и преобразуем его в текст
url = "https://example.com"
html = requests.get(url).text

# Ищем все ссылки на файлы в тексте документа с помощью регулярных выражений
file_links = re.findall(r'(?:href|src)="(.*?\.(pdf|docx?|xlsx?|pptx?|zip|rar|tar\.gz|gz|mp\d))"', html, re.IGNORECASE)

# Выводим найденные ссылки на экран
print("Ссылки на файлы:")
for link, extension in file_links:
    print(link)