from django.contrib.auth import get_user_model

User = get_user_model()


class UserIsFollowerMixin:
    """Флаг 'following' (является ли пользователь подписчиком)."""

    @property
    def extra_context(self):
        author = User.objects.get(username=self.kwargs['username'])

        following = False
        if self.request.user.is_authenticated:
            if self.request.user.follower.filter(author=author).exists():
                following = True
        return {'following': following}
