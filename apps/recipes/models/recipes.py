from django.contrib.auth import get_user_model
from django.db import models

from apps.recipes.models.ingredients import Ingredient
from apps.recipes.models.tags import Tag

_NAME_MAX_LENGTH = 100
User = get_user_model()


class Recipe(models.Model):
    name = models.CharField(
        max_length=_NAME_MAX_LENGTH,
        verbose_name='Название',
    )
    image = models.ImageField(
        upload_to='recipes/',
        verbose_name='Картинка',
    )
    text = models.TextField(verbose_name='Описание')
    cooking_time = models.PositiveIntegerField(
        verbose_name='Время приготовления в минутах',
    )
    created_at = models.DateTimeField(
        auto_now_add=True,
        db_index=True,
        verbose_name='Дата публикации рецепта',
    )

    author = models.ForeignKey(
        to=User,
        on_delete=models.CASCADE,
        related_name='recipes',
        verbose_name='Автор рецепта',
    )
    tags = models.ManyToManyField(to=Tag, verbose_name='Теги')
    ingredients = models.ManyToManyField(
        to=Ingredient,
        through='RecipeIngredient',
        verbose_name='Ингредиенты',
    )

    class Meta:  # noqa: WPS306
        verbose_name = 'Рецепт'
        verbose_name_plural = 'Рецепты'
        ordering = ('-created_at', )

    def __str__(self):
        return self.name


class RecipeIngredient(models.Model):
    ingredient = models.ForeignKey(to=Ingredient, on_delete=models.CASCADE)
    recipe = models.ForeignKey(to=Recipe, on_delete=models.CASCADE)
    amount = models.IntegerField(verbose_name='Количество')

    class Meta:  # noqa: WPS306
        verbose_name = 'Ингридиент рецепта'
        verbose_name_plural = 'Ингридиенты рецепта'

    def __str__(self):
        return self.ingredient.name
