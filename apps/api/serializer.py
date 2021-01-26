from rest_framework import serializers

from apps.recipes.models.favorites import Favorite, Recipe


class FavoriteSerializer(serializers.ModelSerializer):
    id = serializers.PrimaryKeyRelatedField(  # noqa: WPS125
        source='recipe',
        queryset=Recipe.objects.all(),
    )
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta(object):
        model = Favorite
        fields = ('user', 'id')
