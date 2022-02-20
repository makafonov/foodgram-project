from django.db import models


_TAG_MAX_LENGTH = 10
_COLOR_MAX_LENGTH = 6


class TagChoices(models.TextChoices):
    BREAKFAST = 'breakfast', 'Завтрак'  # noqa: WPS115
    LUNCH = 'lunch', 'Обед'  # noqa: WPS115
    DINNER = 'dinner', 'Ужин'  # noqa: WPS115


class ColorChoices(models.TextChoices):
    GREEN = 'green', 'Зеленый'  # noqa: WPS115
    ORANGE = 'orange', 'Оранжевый'  # noqa: WPS115
    PURPLE = 'purple', 'Фиолетовый'  # noqa: WPS115


class Tag(models.Model):
    name = models.CharField(
        max_length=_TAG_MAX_LENGTH,
        choices=TagChoices.choices,
        default=TagChoices.LUNCH,
        unique=True,
        verbose_name='Название',
    )
    color = models.CharField(
        max_length=_COLOR_MAX_LENGTH,
        choices=ColorChoices.choices,
        default=ColorChoices.GREEN,
        unique=True,
        verbose_name='Цвет',
    )

    class Meta:  # noqa: WPS306
        verbose_name = 'Тег'
        verbose_name_plural = 'Теги'

    def __str__(self):
        return self.name
