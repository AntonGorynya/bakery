import os
import json
import logging

import requests

from requests.exceptions import HTTPError
from urllib.parse import urlparse

from cakeorder.models import Advertisement
from django.core.management.base import BaseCommand
from typing import Any, Optional


class Command(BaseCommand):
    help = 'Посчитать количество переходов по ссылкам'
    
    def handle(self, *args: Any, **options: Any):
        access_token = os.environ['BITLY_ACCESS_TOKEN']
        advertisements = Advertisement.objects.all()
        try:
            for advertisement in advertisements:
                url_template = ("https://api-ssl.bitly.com/v4/bitlinks/"
                                "{}/clicks/summary")
                headers = {
                    "Authorization": f"Bearer {access_token}",
                }
                url = advertisement.bitlink
                print(url)
                parsed_bitlink = urlparse(url)
                parsed_bitlink = f"{parsed_bitlink.netloc}{parsed_bitlink.path}"
                url = url_template.format(parsed_bitlink)
                response = requests.get(url, headers=headers)
                response.raise_for_status()
                click_count = response.json()["total_clicks"]
                advertisement.clicks = click_count
                advertisement.save()
        except HTTPError as error:
            logging.exception(error)