from django.core.paginator import Paginator


class PaginatorMixin(object):
    """Паджинатор постов."""

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(object_list=object_list, **kwargs)
        paginator = Paginator(context['object_list'], 10)
        page_number = self.request.GET.get('page')
        context['page'] = paginator.get_page(page_number)
        context['paginator'] = paginator

        return context
