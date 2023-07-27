import os
import json
from django.core.validators import URLValidator
from django.core.exceptions import ValidationError
from django.core.management.base import BaseCommand
import requests

from cakeorder.models import Form, Topping, Berries, Decor


class Command(BaseCommand):
    help = u'Загрузка данных'

    def add_arguments(self, parser):
        parser.add_argument('url', type=str, help=u'Url адрес к Json файлу')

    def handle(self, *args, **options):

        url = options['url']
        val = URLValidator()
        if url:
            try:
                val(url)
                response = requests.get(url)
                response.raise_for_status
                bakery_info = response.json()

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
            except ValidationError:
                print('Проверьте правильность написания ссылки')
            except json.decoder.JSONDecodeError:
                print('По этой ссылке нет информации в требуемом формате JSON')
        else:
            print('Введите ссылку для добавления информации в базу')
