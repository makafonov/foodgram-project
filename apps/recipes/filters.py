import django_filters

from apps.recipes.models import Recipe, Tag


class TagFilterSet(django_filters.FilterSet):
    tags = django_filters.filters.ModelMultipleChoiceFilter(
        queryset=Tag.objects.all(),
        field_name='tags__name',
        to_field_name='name',
    )

    class Meta:  # noqa: WPS306
        model = Recipe
        fields = ('tags',)
