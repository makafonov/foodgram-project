from django.shortcuts import get_object_or_404

from apps.recipes.models import Ingredient, Recipe


def add_ingredients_to_recipe(recipe, ingredients):
    Recipe.ingredients.through.objects.bulk_create(
        [
            Recipe.ingredients.through(
                recipe=recipe,
                ingredient=get_object_or_404(
                    Ingredient,
                    name=ingredient['name'],
                ),
                amount=ingredient['amount'],
            ) for ingredient in ingredients
        ],
    )
