from django import template

from apps.recipes.models import Favorite, Follow, Purchase

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


@register.simple_tag(takes_context=True)
def is_purchase(context):
    return Purchase.objects.filter(
        user=context['user'],
        recipe=context['recipe'],
    ).exists()


@register.simple_tag(takes_context=True)
def param_replace(context, **kwargs):
    query_string = context['request'].GET.copy()
    if 'page' in kwargs:
        query_string['page'] = kwargs.get('page')

    return query_string.urlencode()


@register.simple_tag(takes_context=True)
def manage_tags(context, **kwargs):
    tag = kwargs['tag']
    query_string = context['request'].GET.copy()
    tags = query_string.getlist('tags')
    if tag in tags:
        tags.remove(tag)
    else:
        tags.append(tag)
    query_string.setlist('tags', tags)

    if 'page' in query_string:
        query_string.pop('page')

    return query_string.urlencode()
