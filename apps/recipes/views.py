from django.views.generic import ListView

from apps.recipes.mixins import PaginatorMixin
from apps.recipes.models import Recipe


class IndexView(PaginatorMixin, ListView):
    model = Recipe
    template_name = 'index.html'
    paginate_by = 10
