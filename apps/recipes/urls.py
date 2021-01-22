from django.urls import path

from apps.recipes import views

app_name = 'recipes'

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path(
        '<str:username>/<int:pk>/',
        views.RecipeView.as_view(),
        name='recipe',
    ),
]
