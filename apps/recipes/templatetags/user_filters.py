from django import template

from apps.recipes.models import Favorite, Follow

register = template.Library()


@register.filter
def addclass(field, css):
    return field.as_widget(attrs={'class': css})


@register.simple_tag(takes_context=True)
def is_favorite(context):
    return Favorite.objects.filter(
        user=context['user'],
        recipe=context['recipe'],
    ).exists()


@register.simple_tag(takes_context=True)
def is_follower(context):
    return Follow.objects.filter(
        user=context['user'],
        author=context['author'],
    ).exists()
