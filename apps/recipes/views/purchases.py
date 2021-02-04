from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView

from apps.recipes.models import Recipe


class PurchaseView(LoginRequiredMixin, ListView):
    model = Recipe
    template_name = 'recipes/purchases.html'

    def get_queryset(self):
        queryset = super().get_queryset()
        return queryset.filter(purchases__user=self.request.user)
