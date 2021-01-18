import csv

from django.core.management.base import BaseCommand

from apps.recipes import models


class Command(BaseCommand):
    def handle(self, *args, **options):  # noqa: WPS110
        with open(
            'fixtures/ingredients.csv',
            encoding='utf-8',
        ) as csvfile:
            reader = csv.reader(csvfile)
            for row in reader:
                ingredient = models.Ingredient(title=row[0], dimension=row[1])
                ingredient.save()
