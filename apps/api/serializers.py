from django.contrib.auth import get_user_model
from rest_framework import serializers

from apps.recipes.models import Favorite, Follow, Ingredient, Purchase, Recipe

User = get_user_model()


class FavoriteSerializer(serializers.ModelSerializer):
    id = serializers.PrimaryKeyRelatedField(  # noqa: WPS125
        source='recipe',
        queryset=Recipe.objects.all(),
    )
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:  # noqa: WPS306
        model = Favorite
        fields = ('user', 'id')


class FollowSerializer(serializers.ModelSerializer):
    id = serializers.PrimaryKeyRelatedField(  # noqa: WPS125
        source='author',
        queryset=User.objects.all(),
    )
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:  # noqa: WPS306
        model = Follow
        fields = ('user', 'id')


class PurchaseSerializer(serializers.ModelSerializer):
    id = serializers.PrimaryKeyRelatedField(  # noqa: WPS125
        source='recipe',
        queryset=Recipe.objects.all(),
    )
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:  # noqa: WPS306
        model = Purchase
        fields = ('user', 'id')


class IngredientSerializer(serializers.ModelSerializer):
    title = serializers.CharField(source='name')

    class Meta:  # noqa: WPS306
        model = Ingredient
        fields = ('title', 'dimension')
