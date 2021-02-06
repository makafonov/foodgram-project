from apps.recipes.models import Tag


class TagContextMixin:  # noqa: WPS306
    @property
    def extra_context(self):
        return {
            'active_tags': self.request.GET.getlist('tags'),
            'tags': Tag.objects.all(),
        }
