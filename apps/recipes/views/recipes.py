from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView, DeleteView, DetailView, UpdateView

from apps.recipes.forms import RecipeForm
from apps.recipes.models import Recipe
from apps.recipes.services import add_ingredients_to_recipe
from apps.recipes.views.permissions import PermissionCheck


class RecipeView(DetailView):
    model = Recipe
    template_name = 'recipes/recipe.html'


class RecipeCreateView(LoginRequiredMixin, CreateView):
    model = Recipe
    template_name = 'recipes/add_recipe.html'
    form_class = RecipeForm

    def form_valid(self, form):
        recipe = form.save(commit=False)
        recipe.author = self.request.user
        recipe.save()
        ingredients = form.cleaned_data['ingredients']
        form.cleaned_data['ingredients'] = []
        form.save_m2m()
        add_ingredients_to_recipe(recipe, ingredients)

        return redirect(
            'recipes:recipe',
            username=recipe.author.username,
            pk=recipe.pk,
        )


class RecipeUpdateView(LoginRequiredMixin, PermissionCheck, UpdateView):
    model = Recipe
    template_name = 'recipes/add_recipe.html'
    form_class = RecipeForm

    def form_valid(self, form):
        recipe = form.save(commit=False)
        recipe.ingredients.clear()
        ingredients = form.cleaned_data['ingredients']
        form.cleaned_data['ingredients'] = []
        recipe.save()
        form.save_m2m()
        add_ingredients_to_recipe(recipe, ingredients)

        return redirect(
            'recipes:recipe',
            username=recipe.author.username,
            pk=recipe.pk,
        )


class RecipeDeleteView(LoginRequiredMixin, PermissionCheck, DeleteView):
    model = Recipe
    success_url = reverse_lazy('recipes:index')
