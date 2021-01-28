from django.contrib.auth import get_user_model
from rest_framework import serializers

from apps.recipes.models import Favorite, Follow, Purchase, Recipe

User = get_user_model()


class FavoriteSerializer(serializers.ModelSerializer):
    id = serializers.PrimaryKeyRelatedField(  # noqa: WPS125
        source='recipe',
        queryset=Recipe.objects.all(),
    )
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta(object):
        model = Favorite
        fields = ('user', 'id')


class FollowSerializer(serializers.ModelSerializer):
    id = serializers.PrimaryKeyRelatedField(  # noqa: WPS125
        source='author',
        queryset=User.objects.all(),
    )
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta(object):
        model = Follow
        fields = ('user', 'id')


class PurchaseSerializer(serializers.ModelSerializer):
    id = serializers.PrimaryKeyRelatedField(  # noqa: WPS125
        source='recipe',
        queryset=Recipe.objects.all(),
    )
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta(object):
        model = Purchase
        fields = ('user', 'id')
