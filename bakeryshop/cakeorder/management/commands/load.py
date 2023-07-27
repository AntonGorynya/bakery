# import os

# from django.core.validators import URLValidator
# from django.core.exceptions import ValidationError
from django.core.management.base import BaseCommand
# from django.core.files.base import ContentFile
# import requests
# from urllib.parse import quote, urlparse

# from places.models import Place, Image


# def get_places(url):
    # """Эта функция получает список JSON файлов только с github.com"""
    # response = requests.get(url)
    # response.raise_for_status
    # items = response.json()['payload']['tree']['items']
    # url_places = [item['name'] for item in items]
    # return url_places


# def save_image(place, img_url):
    # response = requests.get(img_url)
    # response.raise_for_status
    # img = ContentFile(response.content)
    # img_path = urlparse(img_url)
    # img_name = os.path.basename(img_path.path)
    # image = Image.objects.create(place=place)
    # image.image.save(img_name, img, save=True)


# def save_place(url):
    # response = requests.get(url)
    # response.raise_for_status
    # place_info = response.json()
    # img_urls = place_info['imgs']
    # place, created = Place.objects.get_or_create(
        # title=place_info['title'],
        # description_short=place_info['description_short'],
        # description_long=place_info['description_long'],
        # lng=float(place_info['coordinates']['lng']),
        # lat=float(place_info['coordinates']['lat']),
    # )

    # return place, created, img_urls



class Command(BaseCommand):
    help = u'Загрузка данных об интересных местах Москвы'

    # def add_arguments(self, parser):
        # parser.add_argument('-url', type=str, help=u'Url адрес к Json файлу')
        # parser.add_argument('-git_url', type=str, help=u'Адрес на github к Json файлам')

    def handle(self, *args, **options):
        print('Проверка')
        # url = options['url']
        # git_url = options['git_url']
        # val = URLValidator()
        # if url:
            # try:
                # val(url)
                # place, created, img_urls = save_place(url)
                # if created:
                    # for img_url in img_urls:
                        # save_image(place, img_url)
                    # print(f'Скачаны информация об объекте {place.title}')
                    # print(f'и фотографии в количестве {place.images.count()} штук')
                # else:
                    # print(f'Объект {place.title} в базе уже есть')
            # except ValidationError:
                # print('Проверьте правильность написания ссылки')
            # except requests.exceptions.JSONDecodeError:
                # print('По этой ссылке нет информации в требуемом формате JSON')
        # elif git_url:
            # try:
                # val(git_url)
                # url_places = get_places(git_url)
                # for name_place in url_places:
                    # url_place = f'https://raw.githubusercontent.com/devmanorg/where-to-go-places/master/places/{quote(name_place)}'
                    # place, created, img_urls = save_place(url_place)
                    # if created:
                        # for img_url in img_urls:
                            # save_image(place, img_url)
                        # print(f'Скачаны информация об объекте {place.title}')
                        # print(f'и фотографии в количестве {place.images.count()} штук')
                    # else:
                        # print(f'Объект {place.title} в базе уже есть')
            # except ValidationError:
                # print('Проверьте правильность написания ссылки')
            # except requests.exceptions.JSONDecodeError:
                # print('По этой ссылке нет информации в требуемом формате JSON')
        # else:
            # print('Введите ссылку для добавления информации в базу')
