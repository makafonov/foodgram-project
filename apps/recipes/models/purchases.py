from django.contrib.auth import get_user_model
from django.db import models

from apps.recipes.models.recipes import Recipe

User = get_user_model()


class Purchase(models.Model):
    """Model definition for Purchase."""

    user = models.ForeignKey(
        to=User,
        verbose_name='Пользователь',
        on_delete=models.CASCADE,
        related_name='purchases',
    )
    recipe = models.ForeignKey(
        to=Recipe,
        verbose_name='Рецепт',
        on_delete=models.CASCADE,
        related_name='purchases',
    )

    class Meta:  # noqa: WPS306
        """Meta definition for Purchase."""

        verbose_name = 'Покупка'
        verbose_name_plural = 'Покупки'
        constraints = [
            models.UniqueConstraint(
                fields=['user', 'recipe'],
                name='unique_purchase_user_recipe',
            ),
        ]

    def __str__(self):
        """Unicode representation of Purchase."""
        return '{0} -> {1}'.format(self.user.username, self.recipe.name)
