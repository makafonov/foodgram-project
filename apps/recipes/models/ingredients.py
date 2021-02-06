from django.db import models

_TITLE_MAX_LENGTH = 100
_DIMENSION_MAX_LENGTH = 20


class Ingredient(models.Model):
    name = models.CharField(
        max_length=_TITLE_MAX_LENGTH,
        verbose_name='Наименование',
    )
    dimension = models.CharField(
        max_length=_DIMENSION_MAX_LENGTH,
        verbose_name='Единицы измерения',
    )

    class Meta:  # noqa: WPS306
        verbose_name = 'Ингредиент'
        verbose_name_plural = 'Ингредиенты'

    def __str__(self):
        return '{0}, {1}'.format(self.name, self.dimension)
