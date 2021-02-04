from django.contrib.auth import get_user_model
from django.views.generic import DetailView
from django.views.generic.list import MultipleObjectMixin

from apps.recipes.models import Recipe

User = get_user_model()


class ProfileView(DetailView, MultipleObjectMixin):
    model = User
    template_name = 'recipes/profile.html'
    paginate_by = 6
    context_object_name = 'profile_user'
    slug_field = 'username'
    slug_url_kwarg = 'username'

    def get_context_data(self, **kwargs):
        object_list = Recipe.objects.filter(author=self.get_object())
        return super().get_context_data(object_list=object_list, **kwargs)

    @property
    def extra_context(self):
        """Flag user_is_follower."""
        author = User.objects.get(username=self.kwargs['username'])

        is_follower = False
        if self.request.user.is_authenticated:
            if self.request.user.follower.filter(author=author).exists():
                is_follower = True
        return {'user_is_follower': is_follower}
