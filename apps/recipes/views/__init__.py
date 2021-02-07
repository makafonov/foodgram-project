# flake8: noqa
from apps.recipes.views.favorites import FavoriteView
from apps.recipes.views.index import IndexView
from apps.recipes.views.profile import ProfileView
from apps.recipes.views.purchases import DownloadPurchasesListView, PurchaseView
from apps.recipes.views.recipes import (
    RecipeCreateView,
    RecipeDeleteView,
    RecipeUpdateView,
    RecipeView,
)
from apps.recipes.views.subscribers import FollowView
