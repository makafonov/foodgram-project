from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView
from django_filters.views import BaseFilterView

from apps.recipes.filters import TagFilterSet
from apps.recipes.models import Recipe
from apps.recipes.views.mixins import TagContextMixin


class FavoriteView(
    LoginRequiredMixin,
    TagContextMixin,
    BaseFilterView,
    ListView,
):
    model = Recipe
    template_name = 'recipes/favorites.html'
    paginate_by = 6
    filterset_class = TagFilterSet

    def get_queryset(self):
        queryset = super().get_queryset()
        return queryset.filter(favorites__user=self.request.user)
