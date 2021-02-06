import io

from django.db.models import Sum
from django.shortcuts import get_object_or_404
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.pdfgen.canvas import Canvas

from apps.recipes.models import Ingredient, Recipe, RecipeIngredient


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


def generate_pdf(user):
    ingredients = RecipeIngredient.objects.filter(
        recipe__purchases__user=user,
    ).values(
        'ingredient__name',
        'ingredient__dimension',
    ).annotate(amount=Sum('amount'))
    buffer = io.BytesIO()
    canvas = Canvas(buffer, bottomup=0)

    pdfmetrics.registerFont(
        TTFont(
            'Montserrat',
            'static/recipes/fonts/Montserrat-Regular.ttf',
        ),
    )

    title = 'Список покупок | Foodgram'
    canvas.setTitle(title)
    x = y = 50

    canvas.setFont('Montserrat', 18)
    canvas.drawString(x, y, title)

    canvas.setFont('Montserrat', 14)
    canvas.drawString(x, y + 50, 'Продукты:')

    y = 130
    canvas.setFont('Montserrat', 12)
    for ingredient in ingredients:
        line = '{0} {1} {2}'.format(
            ingredient['ingredient__name'],
            ingredient['amount'],
            ingredient['ingredient__dimension'],
        )
        canvas.drawString(x, y, line)
        y += 25

    canvas.showPage()
    canvas.save()
    buffer.seek(0)

    return buffer
