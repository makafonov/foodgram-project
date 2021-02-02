from django import forms

from apps.recipes.models import Recipe, Tag


class RecipeForm(forms.ModelForm):
    tags = forms.ModelMultipleChoiceField(
        label='Теги',
        queryset=Tag.objects.all(),
        widget=forms.CheckboxSelectMultiple,
    )

    class Meta(object):
        model = Recipe
        fields = (
            'name',
            'tags',
            'ingredients',
            'cooking_time',
            'text',
            'image',
        )
        labels = {
            'name': 'Название рецепта',
            'cooking_time': 'Время приготовления',
            'image': 'Загрузить фото',
        }
        widgets = {
            'cooking_time': forms.TextInput(),
            'ingredients': forms.TextInput(attrs={'id': 'nameIngredient'}),
        }
