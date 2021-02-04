from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView

from apps.recipes.models import Recipe


class FavoriteView(LoginRequiredMixin, ListView):
    model = Recipe
    template_name = 'recipes/favorites.html'
    paginate_by = 6

    def get_queryset(self):
        queryset = super().get_queryset()
        return queryset.filter(favorites__user=self.request.user)
