import os
import json
import logging


import requests

from requests.exceptions import HTTPError

from cakeorder.models import Advertisement
from django.core.management.base import BaseCommand
from typing import Any


class Command(BaseCommand):
    help = 'Сформировать набор ссылок bitly'
    
    def handle(self, *args: Any, **options: Any) -> str | None:
        access_token = os.environ["BITLY_ACCESS_TOKEN"]
        try:
            links = json.loads(os.environ['LINKS'])
            for link in links:
                url_template = "https://api-ssl.bitly.com/v4/bitlinks"
                headers = {
                    "Authorization": f"Bearer {access_token}",
                }
                payload = {
                    "long_url": link,
                }
                response = requests.post(url_template, headers=headers, json=payload)
                response.raise_for_status()
                bitlink = response.json()["link"]
                Advertisement.objects.update_or_create(link=link, bitlink=bitlink)
                print(link)
                print(bitlink)
        except HTTPError as error:
            logging.exception(error)
