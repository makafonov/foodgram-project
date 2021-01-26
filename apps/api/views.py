from rest_framework import mixins, status, viewsets
from rest_framework.response import Response

from apps.api.serializer import FavoriteSerializer
from apps.recipes.models import Favorite


class FavoriteApiView(
    mixins.CreateModelMixin,
    mixins.DestroyModelMixin,
    viewsets.GenericViewSet,
):
    queryset = Favorite.objects.all()
    serializer_class = FavoriteSerializer
    lookup_field = 'recipe'

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        is_deleted = instance.delete()
        if is_deleted:
            return Response({'success': True}, status=status.HTTP_200_OK)
        return Response({'success': False})
