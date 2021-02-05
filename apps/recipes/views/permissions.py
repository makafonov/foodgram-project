from django.shortcuts import redirect


class PermissionCheck(object):
    def dispatch(self, request, *args, **kwargs):
        if not self.request.user.is_superuser:
            if self.request.user.username != self.kwargs['username']:
                return redirect(
                    'recipes:recipe',
                    username=self.kwargs['username'],
                    pk=self.kwargs['pk'],
                )
        return super().dispatch(request, *args, **kwargs)
