from django.views.generic import ListView

from apps.recipes.mixins import PaginatorMixin
from apps.recipes.models import Recipe


class IndexView(PaginatorMixin, ListView):
    model = Recipe
    template_name = 'recipes/index.html'
    paginate_by = 10
