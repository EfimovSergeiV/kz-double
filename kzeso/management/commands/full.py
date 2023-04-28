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

def create_path(path_dir):
    """ Создаём путь, если отсутствует """
    if not os.path.exists(os.path.dirname(path_dir)):
        try:
            os.makedirs(os.path.dirname(path_dir))
        except OSError:
            raise

def download_file(from_url, to_url):
    """ Загружаем и сохраняем файл """
    response = requests.get(from_url)
    with open(to_url, 'wb') as f:
        f.write(response.content)

completed = [
    # '/home/anon/dev/k-double/kzeso/templates//contacts.html',
    # '/home/anon/dev/k-double/kzeso/templates//index.html',
    # '/home/anon/dev/k-double/kzeso/templates//sitemap.xml',
    # '/home/anon/dev/k-double/kzeso/templates//about.html',
]

count = 0

for root, dirs, files in os.walk(f'{BASE_DIR}/kzeso/templates/'):  
    for filename in files:
        file = f'{root}/{filename}'.replace('//', '/')

        if file not in completed:
            
            count += 1
            print( f'{count}. Открываем: {file}')


            with open(file) as fp:
                soup = BeautifulSoup(fp, "html.parser")

            # Search styles and images in document
            for link in soup.find_all('link'):
                href = link.get('href')
                if href:

                    css = True if '.css' in href else False
                    png = True if '.png' in href else False

                    if css or png:
                        script_path = href.replace('https://kzeso.com/', '').replace('//kzeso.com/', '')
                        from_url = f'https://kzeso.com/{ script_path }'
                        to_url = f'{ BASE_DIR }/kzeso/static/{ script_path }'

                        static_value = "{% static " + f"'{ script_path }'" + " %}"

                        # {% 'wp-content/plugins/js_composer/assets/css/js_composer.min?ver=6.0.3.css' %}
                        if static_value == "{% static 'wp-content/plugins/js_composer/assets/css/js_composer.min.css?ver=6.0.3' %}":
                            static_value = static_value.replace('js_composer.min.css?ver=6.0.3', 'js_composer.min?ver=6.0.3.css')

                        print(f'From:\t{from_url}')
                        print(f'To:\t{to_url}')
                        print(static_value)
                        print('\n')
                        

                        create_path(path_dir=to_url)
                        download_file(from_url=from_url, to_url=to_url)
                        link['href'] = static_value

            print("Parsing images:")
            sleep(2)

            for img in soup.find_all('img'):
                src = img.get('src')
                if src:
                    image_path = src.replace('https://kzeso.com/', '').replace('//kzeso.com/', '')
                    from_url = f'https://kzeso.com/{ image_path }'
                    to_url = f'{ BASE_DIR }/kzeso/static/{ image_path }'
                    static_value = "{% static " + f"'{ image_path }'" + " %}"

                    print(f'From:\t{from_url}')
                    print(f'To:\t{to_url}')
                    print(static_value)
                    print('\n')

                    create_path(path_dir=to_url)
                    download_file(from_url=from_url, to_url=to_url)
                    img['src'] = static_value

            print("Parsing scripts:")
            sleep(2)

            for script in soup.find_all('script'):
                src = script.get('src')
                if src:
                    image_path = src.replace('https://kzeso.com/', '').replace('//kzeso.com/', '')
                    from_url = f'https://kzeso.com/{ image_path }'
                    to_url = f'{ BASE_DIR }/kzeso/static/{ image_path }'
                    static_value = "{% static " + f"'{ image_path }'" + " %}"

                    print(f'From:\t{from_url}')
                    print(f'To:\t{to_url}')
                    print(static_value)
                    print('\n')

                    create_path(path_dir=to_url)
                    download_file(from_url=from_url, to_url=to_url)
                    script['src'] = static_value


            # Перезаписываем документ
            with open(file, "w") as fp:
                fp.write(str(soup))


            print(f"Документ { file } готов!")
            sleep(2)

