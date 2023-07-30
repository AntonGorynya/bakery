import os
import json
from django.core.validators import URLValidator
from django.core.exceptions import ValidationError
from django.core.management.base import BaseCommand
from django.core.files.base import ContentFile
import requests
from urllib.parse import urlparse
from cakeorder.models import Levels_number, Form, Topping, Berries, Decor, Cake


def save_image(cake, img_url):
    response = requests.get(img_url)
    response.raise_for_status
    img = ContentFile(response.content)
    img_path = urlparse(img_url)
    img_name = os.path.basename(img_path.path)
    cake.image.save(img_name, img, save=True)


class Command(BaseCommand):
    help = u'Загрузка данных'

    def add_arguments(self, parser):
        parser.add_argument(
            '-url', type=str, help=u'Url адрес к Json файлу',
            default='https://raw.githubusercontent.com/Amartyanov1974/bakery-data/main/data_bakery.json',
            )

    def handle(self, *args, **options):

        url = options['url']
        val = URLValidator()
        if url:
            try:
                val(url)
                response = requests.get(url)
                response.raise_for_status
                bakery_info = response.json()

                for position in bakery_info['Levels_number']:
                    unit, created = Levels_number.objects.get_or_create(
                        quantity=position['num'], price=position['price'])
                    if created:
                        print(f'В базу добавили {unit.quantity}')

                for position in bakery_info['Form']:
                    unit, created = Form.objects.get_or_create(
                        name=position['name'], price=position['price'])
                    if created:
                        print(f'В базу добавили {unit.name}')

                for position in bakery_info['Topping']:
                    unit, created = Topping.objects.get_or_create(
                        name=position['name'], price=position['price'])
                    if created:
                        print(f'В базу добавили {unit.name}')

                for position in bakery_info['Berries']:
                    unit, created = Berries.objects.get_or_create(
                        name=position['name'], price=position['price'])
                    if created:
                        print(f'В базу добавили {unit.name}')

                for position in bakery_info['Decor']:
                    unit, created = Decor.objects.get_or_create(
                        name=position['name'], price=position['price'])
                    if created:
                        print(f'В базу добавили {unit.name}')
                for cake in bakery_info['Cake']:
                    unit, created = Cake.objects.get_or_create(
                        name=cake['name'], price=cake['price'],
                        occasion=cake['occasion'] , type=cake['type'])
                    if created:
                        img_url=cake['image']
                        save_image(unit, img_url)
                        print(f'В базу добавили {unit.name}')

            except ValidationError:
                print('Проверьте правильность написания ссылки')
            except json.decoder.JSONDecodeError:
                print('По этой ссылке нет информации в требуемом формате JSON')
        else:
            print('Введите ссылку для добавления информации в базу')
