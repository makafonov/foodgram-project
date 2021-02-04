from django.contrib.auth import get_user_model
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView


class FollowView(LoginRequiredMixin, ListView):
    model = get_user_model()
    template_name = 'recipes/follow.html'
    paginate_by = 6

    def get_queryset(self):
        queryset = super().get_queryset()
        return queryset.filter(  # yapf: disable
            following__user=self.request.user,
        ).order_by('-id')
