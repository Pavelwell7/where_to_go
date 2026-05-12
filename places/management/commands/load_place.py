import os
import requests

from urllib.parse import urlparse
from django.core.files.base import ContentFile
from django.core.management.base import BaseCommand

from places.models import Place, Image


class Command(BaseCommand):
    help = 'Загружает место из JSON файла по URL'

    def add_arguments(self, parser):
        parser.add_argument('url', type=str, help='URL JSON файла с данными о месте')

    def handle(self, *args, **options):
        url = options['url']

        response = requests.get(url)
        response.raise_for_status()
        place_data = response.json()

        place, created = Place.objects.get_or_create(
            title=place_data['title'],
            defaults={
                'short_description': place_data.get('short_description', ''),
                'long_description': place_data.get('long_description', ''),
                'lat': place_data['coordinates']['lat'],
                'lng': place_data['coordinates']['lng'],
            }
        )

        if not created:
            self.stdout.write(f'Место уже существует: {place.title}')
            return

        for order, img_url in enumerate(place_data.get('imgs', [])):
            img_response = requests.get(img_url)
            img_response.raise_for_status()

            filename = os.path.basename(urlparse(img_url).path)
            image = Image(place=place, order=order)
            image.image.save(filename, ContentFile(img_response.content), save=True)

        self.stdout.write(self.style.SUCCESS(f'Загружено: {place.title}'))
