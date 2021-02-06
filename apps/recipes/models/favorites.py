from django.contrib.auth import get_user_model
from django.db import models

from apps.recipes.models.recipes import Recipe

User = get_user_model()


class Favorite(models.Model):
    """Model definition for Favorite."""

    user = models.ForeignKey(
        to=User,
        verbose_name='Пользователь',
        on_delete=models.CASCADE,
        related_name='favorites',
    )
    recipe = models.ForeignKey(
        to=Recipe,
        verbose_name='Рецепт',
        on_delete=models.CASCADE,
        related_name='favorites',
    )

    class Meta:  # noqa: WPS306
        """Meta definition for Favorite."""

        verbose_name = 'Избранное'
        verbose_name_plural = 'Избранные'
        constraints = [
            models.UniqueConstraint(
                fields=['user', 'recipe'],
                name='unique_favorite_user_recipe',
            ),
        ]

    def __str__(self):
        """Unicode representation of Favorite."""
        return '{0} -> {1}'.format(self.user.username, self.recipe.name)
