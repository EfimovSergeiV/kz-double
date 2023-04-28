from django.core.management.base import BaseCommand, CommandError
from bs4 import BeautifulSoup
import requests, os, re
from time import sleep

from django.conf import settings
from django.conf.urls.static import static


BASE_DIR = settings.BASE_DIR

class Command(BaseCommand):
    args = ''
    help = ''

    def handle(self, *args, **options):
        pass

# def create_path(path_dir):
#     """ Создаём путь, если отсутствует """
#     if not os.path.exists(os.path.dirname(path_dir)):
#         try:
#             os.makedirs(os.path.dirname(path_dir))
#         except OSError:
#             raise

# def download_file(from_url, to_url):
#     """ Загружаем и сохраняем файл """
#     response = requests.get(from_url)
#     with open(to_url, 'wb') as f:
#         f.write(response.content)


# count = 0

# list_files = []

# for root, dirs, files in os.walk(f'{BASE_DIR}/kzeso/templates/'):  
#     for filename in files:
#         file = f'{root}/{filename}'.replace('//', '/')

#         if file:
            
#             count += 1
#             print( f'{count}. Открываем: {file}')


#             with open(file) as fp:
#                 soup = BeautifulSoup(fp, "html.parser")

#             # Search styles and images in document
#             for link in soup.find_all('link'):
#                 href = link.get('href')
#                 if href:

#                     css = True if '.css' in href else False
#                     # png = True if '.png' in href else False

#                     if css:

#                         result = re.sub(r'\?ver=\d+\.\d+\.\d+', '', href)
#                         new_href = re.sub(r'\?ver=\d+', '', result)
#                         print(new_href)

#                         if new_href not in list_files:
#                             list_files.append(new_href)
#                         # script_path = href.replace('https://kzeso.com/', '').replace('//kzeso.com/', '')
#                         # from_url = f'https://kzeso.com/{ script_path }'
#                         # to_url = f'{ BASE_DIR }/kzeso/static/{ script_path }'

#                         # static_value = "{% static " + f"'{ script_path }'" + " %}"

#                         # # {% 'wp-content/plugins/js_composer/assets/css/js_composer.min?ver=6.0.3.css' %}
#                         # if static_value == "{% static 'wp-content/plugins/js_composer/assets/css/js_composer.min.css?ver=6.0.3' %}":
#                         #     static_value = static_value.replace('js_composer.min.css?ver=6.0.3', 'js_composer.min?ver=6.0.3.css')

#                         # print(f'From:\t{from_url}')
#                         # print(f'To:\t{to_url}')
#                         # print(static_value)
#                         # print('\n')
                        

#                         # create_path(path_dir=to_url)
#                         # download_file(from_url=from_url, to_url=to_url)
#                         link['href'] = new_href



#             # # Перезаписываем документ
#             with open(file, "w") as fp:
#                 fp.write(str(soup))


#             # print(f"Документ { file } готов!")
#             # sleep(2)

# print(list_files)




for root, dirs, files in os.walk(f'{BASE_DIR}/kzeso/templates/'):  
    for filename in files:
        file = f'{root}/{filename}'.replace('//', '/')

        if file:

            print(file)

            with open(file, 'r') as f:
                html = f.read()


                new_string = '{% load static %}\n\n'

                # Находим DOCTYPE с помощью регулярного выражения и добавляем новую строку перед ним
                pattern = re.compile(r'<!DOCTYPE.*?>', re.DOTALL)
                html = re.sub(pattern, new_string + r'\g<0>', html)

                # Сохраняем изменения в файл
                with open(file, 'w') as f:
                    f.write(html)
