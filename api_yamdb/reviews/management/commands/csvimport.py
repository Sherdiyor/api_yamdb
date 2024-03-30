import csv
import logging
import os

from django.conf import settings
from django.core.management.base import BaseCommand

from reviews.models import (Category, Comment, Genre, Review, Title,
                            TitleGenre, User)

PATH_DATA = os.path.join(settings.BASE_DIR, 'static/data')
FILES_TO_MODELS = {
    'genre.csv': Genre,
    'titles.csv': Title,
    'category.csv': Category,
    'review.csv': Review,
    'comments.csv': Comment,
    'users.csv': User,
    'genre_title.csv': TitleGenre
}


class Command(BaseCommand):

    def handle(self, *args, **options):
        for name, model in FILES_TO_MODELS.items():
            path = os.path.join(PATH_DATA, name)

            with open(path, 'r', encoding='utf8') as file:
                reader = csv.DictReader(file)
                try:
                    model.objects.bulk_create(
                        model(**data) for data in reader
                    )
                    logging.info('Все данные загружены!')
                except Exception as e:
                    logging.error(e)
