from django.contrib.auth import get_user_model
from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Exists, OuterRef
from django.shortcuts import get_object_or_404, redirect, render
from django.views.generic import CreateView, DetailView, ListView
from django.views.generic.list import MultipleObjectMixin
from django_filters.views import BaseFilterView

from apps.recipes.filters import TagFilterSet
from apps.recipes.forms import RecipeForm
from apps.recipes.models import Favorite, Ingredient, Purchase, Recipe, Tag

_HTTP404 = 404
_HTTP500 = 500
User = get_user_model()


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

        Recipe.ingredients.through.objects.bulk_create(
            [
                Recipe.ingredients.through(
                    recipe=recipe,
                    ingredient=get_object_or_404(
                        Ingredient,
                        name=ingredient['name'],
                    ),
                    amount=ingredient['amount'],
                ) for ingredient in ingredients
            ],
        )
        return redirect(
            'recipes:recipe',
            username=recipe.author.username,
            pk=recipe.pk,
        )


class FavoriteView(LoginRequiredMixin, ListView):
    model = Recipe
    template_name = 'recipes/favorites.html'
    paginate_by = 6

    def get_queryset(self):
        queryset = super().get_queryset()
        return queryset.filter(favorites__user=self.request.user)


class FollowView(LoginRequiredMixin, ListView):
    model = User
    template_name = 'recipes/follow.html'
    paginate_by = 6

    def get_queryset(self):
        queryset = super().get_queryset()
        return queryset.filter(  # yapf: disable
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
        """Flag user_is_follower."""
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


def get_purchases_count(request):
    """Custom template tag for amount of purchases."""
    purchases = Purchase.objects.filter(user=request.user).count()
    return {'user_purchases_count': purchases}


def page_not_found(request, exception):
    return render(
        request,
        'misc/404.html',
        {'path': request.path},
        status=_HTTP404,
    )


def server_error(request):
    return render(request, 'misc/500.html', status=_HTTP500)
