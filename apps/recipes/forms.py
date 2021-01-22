from django import forms

from apps.recipes.models import Recipe, Tag


class RecipeForm(forms.ModelForm):
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
        widgets = {'tags': forms.CheckboxSelectMultiple()}

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['cooking_time'].label = 'Время приготовления'
        self.fields['image'].label = 'Загрузить фото'
