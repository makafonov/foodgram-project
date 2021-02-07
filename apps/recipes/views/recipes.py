from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import CreateView, DeleteView, DetailView, UpdateView

from apps.recipes.forms import RecipeForm
from apps.recipes.models import Recipe
from apps.recipes.views.permissions import PermissionCheck


class RecipeView(DetailView):
    model = Recipe
    template_name = 'recipes/recipe.html'


class RecipeCreateView(LoginRequiredMixin, CreateView):
    model = Recipe
    template_name = 'recipes/add_recipe.html'
    form_class = RecipeForm
    success_url = reverse_lazy('recipes:index')

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class RecipeUpdateView(LoginRequiredMixin, PermissionCheck, UpdateView):
    model = Recipe
    template_name = 'recipes/add_recipe.html'
    form_class = RecipeForm
    success_url = reverse_lazy('recipes:index')


class RecipeDeleteView(LoginRequiredMixin, PermissionCheck, DeleteView):
    model = Recipe
    success_url = reverse_lazy('recipes:index')
