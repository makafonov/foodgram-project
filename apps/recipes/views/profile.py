from django.contrib.auth import get_user_model
from django.shortcuts import get_object_or_404
from django.views.generic import ListView
from django_filters.views import BaseFilterView

from apps.recipes.filters import TagFilterSet
from apps.recipes.models import Recipe
from apps.recipes.views.mixins import TagContextMixin


User = get_user_model()


class ProfileView(TagContextMixin, BaseFilterView, ListView):
    model = Recipe
    template_name = 'recipes/profile.html'
    paginate_by = 6
    filterset_class = TagFilterSet

    def get_queryset(self):
        queryset = super().get_queryset()
        author = get_object_or_404(User, username=self.kwargs['username'])

        return queryset.filter(author=author)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        author = get_object_or_404(User, username=self.kwargs['username'])
        is_follower = False
        if self.request.user.is_authenticated:
            if self.request.user.follower.filter(author=author).exists():
                is_follower = True
        context['user_is_follower'] = is_follower
        context['author'] = author

        return context
