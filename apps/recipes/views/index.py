from django.db.models import Exists, OuterRef
from django.views.generic import ListView
from django_filters.views import BaseFilterView

from apps.recipes.filters import TagFilterSet
from apps.recipes.models import Favorite, Purchase, Recipe, Tag


class IndexView(BaseFilterView, ListView):
    model = Recipe
    template_name = 'recipes/index.html'
    paginate_by = 6
    filterset_class = TagFilterSet

    def get_queryset(self):
        queryset = super().get_queryset()

        if self.request.user.is_authenticated:
            queryset = queryset.annotate(
                is_favorite=Exists(
                    Favorite.objects.filter(
                        user=self.request.user,
                        recipe=OuterRef('pk'),
                    ),
                ),
            ).annotate(
                is_purchase=Exists(
                    Purchase.objects.filter(
                        user=self.request.user,
                        recipe=OuterRef('pk'),
                    ),
                ),
            )
        return queryset

    @property
    def extra_context(self):
        return {
            'active_tags': self.request.GET.getlist('tags'),
            'tags': Tag.objects.all(),
        }
