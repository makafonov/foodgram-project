from django.db import models

_TAG_MAX_LENGTH = 10


class TagChoices(models.TextChoices):
    BREAKFAST = 'завтрак', 'Завтрак'  # noqa: WPS115
    LUNCH = 'обед', 'Обед'  # noqa: WPS115
    DINNER = 'ужин', 'Ужин'  # noqa: WPS115


class Tag(models.Model):
    description = models.CharField(
        max_length=_TAG_MAX_LENGTH,
        choices=TagChoices.choices,
        default=TagChoices.LUNCH,
        unique=True,
        verbose_name='Описание',
    )

    class Meta(object):
        verbose_name = 'Тег'
        verbose_name_plural = 'Теги'

    def __str__(self):
        return self.description
