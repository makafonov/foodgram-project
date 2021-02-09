from django import forms

from apps.recipes.models import Recipe, Tag
from apps.recipes.services import add_ingredients_to_recipe


class RecipeForm(forms.ModelForm):
    tags = forms.ModelMultipleChoiceField(
        label='Теги',
        queryset=Tag.objects.all(),
        widget=forms.CheckboxSelectMultiple,
    )
    ingredients = forms.CharField(
        required=False,
        label='Ингредиенты',
        widget=forms.TextInput(attrs={'id': 'nameIngredient'}),
    )

    class Meta:  # noqa: WPS306
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
        }

    def clean_ingredients(self):
        ingredients = list(
            zip(
                self.data.getlist('nameIngredient'),  # type: ignore
                self.data.getlist('valueIngredient'),  # type: ignore
            ),
        )
        if not ingredients:
            raise forms.ValidationError('Отсутствуют ингредиенты')

        ingredients_clean = []
        for name, amount in ingredients:
            if int(amount) < 1:
                raise forms.ValidationError(
                    'Исправьте количество ингредиента "{0}"'.format(name),
                )
            else:
                ingredients_clean.append({
                    'name': name,
                    'amount': amount,
                })

        return ingredients_clean

    def save(self, commit=True):
        instance = super().save(commit=False)
        instance.save()
        ingredients = self.cleaned_data['ingredients']
        self.cleaned_data['ingredients'] = []
        self.save_m2m()
        add_ingredients_to_recipe(self.instance, ingredients)

        return instance
