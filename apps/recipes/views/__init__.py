# flake8: noqa
from apps.recipes.views.errors import page_not_found, server_error
from apps.recipes.views.favorites import FavoriteView
from apps.recipes.views.index import IndexView
from apps.recipes.views.profile import ProfileView
from apps.recipes.views.purchases import PurchaseView
from apps.recipes.views.recipes import (
    RecipeCreateView,
    RecipeDeleteView,
    RecipeUpdateView,
    RecipeView,
)
from apps.recipes.views.subscribers import FollowView
