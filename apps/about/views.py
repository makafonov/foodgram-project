from django.views.generic.base import TemplateView


class AboutAuthorView(TemplateView):
    template_name = 'about/base.html'
    extra_context = {
        'title': 'Об авторе',
        'content': '@makafonov',
    }


class AboutTechView(TemplateView):
    template_name = 'about/base.html'
    extra_context = {
        'title': 'Технологии',
        'content': 'python, django, djangorestframework',
    }
