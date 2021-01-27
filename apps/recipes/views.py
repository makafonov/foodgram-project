from django.contrib.auth import get_user_model
from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Exists, OuterRef
from django.urls import reverse_lazy
from django.views.generic import CreateView, DetailView, ListView
from django.views.generic.list import MultipleObjectMixin

from apps.recipes.forms import RecipeForm
from apps.recipes.models import Favorite, Recipe

User = get_user_model()


class IndexView(ListView):
    model = Recipe
    template_name = 'recipes/index.html'
    paginate_by = 9

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
            )
        return queryset


class RecipeView(DetailView):
    model = Recipe
    template_name = 'recipes/recipe.html'


class RecipeCreateView(LoginRequiredMixin, CreateView):
    model = Recipe
    template_name = 'recipes/add_recipe.html'
    form_class = RecipeForm
    success_url = reverse_lazy('index')

    def form_valid(self, form):
        form.instance.author = self.request.user
        form.save()
        return super().form_valid(form)


class FavoriteView(LoginRequiredMixin, ListView):
    model = Recipe
    template_name = 'recipes/favorites.html'
    paginate_by = 9

    def get_queryset(self):
        queryset = super().get_queryset()
        return queryset.filter(favorites__user=self.request.user)


class FollowView(LoginRequiredMixin, ListView):
    model = User
    template_name = 'recipes/follow.html'
    paginate_by = 9

    def get_queryset(self):
        queryset = super().get_queryset()
        return queryset.filter(
            following__user=self.request.user,
        ).order_by('-id')


class ProfileView(DetailView, MultipleObjectMixin):
    model = User
    template_name = 'recipes/profile.html'
    paginate_by = 6
    context_object_name = 'profile_user'
    slug_field = 'username'
    slug_url_kwarg = 'username'

    def get_context_data(self, **kwargs):
        object_list = Recipe.objects.filter(author=self.get_object())
        return super().get_context_data(object_list=object_list, **kwargs)

    @property
    def extra_context(self):
        """Флаг user_is_follower. Является ли пользователь подписчиком."""
        author = User.objects.get(username=self.kwargs['username'])

        is_follower = False
        if self.request.user.is_authenticated:
            if self.request.user.follower.filter(author=author).exists():
                is_follower = True
        return {'user_is_follower': is_follower}


class PurchaseView(LoginRequiredMixin, ListView):
    model = Recipe
    template_name = 'recipes/purchases.html'

    def get_queryset(self):
        queryset = super().get_queryset()
        return queryset.filter(purchases__user=self.request.user)
