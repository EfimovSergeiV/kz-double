from django.core.management.base import BaseCommand, CommandError
from bs4 import BeautifulSoup
import requests, os

from django.conf import settings
from django.conf.urls.static import static
from time import sleep

BASE_DIR = settings.BASE_DIR

class Command(BaseCommand):
    args = ''
    help = ''

    def handle(self, *args, **options):
        pass

def create_dir(path):
    # Создание директории, если она не существует
    if not os.path.exists(os.path.dirname(path)):
        try:
            os.makedirs(os.path.dirname(path))
        except OSError:
            raise


def download(url, path):
   # Скачивание файла
    response = requests.get(url)
    with open(path, 'wb') as f:
        f.write(response.content)


with open(f'{BASE_DIR}/kzeso/templates/sitemap.xml') as fp:
    soup = BeautifulSoup(fp,features='xml')


names = soup.find_all('url')
for name in names:

    url = str(name.loc).replace('<loc>', '').replace('</loc>', '')
    path_file = f"{BASE_DIR}/kzeso/templates/{url.replace('https://kzeso.com/', '')[:-1]}.html"
    
    en_url = f'{url.replace("https://kzeso.com/","https://kzeso.com/en/")}'
    en_file = f'{BASE_DIR}/kzeso/templates{en_url.replace("https://kzeso.com", "")[:-1]}.html'
    
    print(en_file)
    
    create_dir(path_file)
    download(url=url, path=path_file)

    create_dir(en_file)
    download(url=en_url, path=en_file)

    sleep(1)