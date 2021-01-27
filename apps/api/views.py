from django.shortcuts import get_object_or_404
from rest_framework import mixins, viewsets
from rest_framework.response import Response

from apps.api.serializer import FavoriteSerializer, FollowSerializer
from apps.recipes.models import Favorite, Follow


class BaseInstanceView(
    mixins.CreateModelMixin,
    mixins.DestroyModelMixin,
    viewsets.GenericViewSet,
):
    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            self.perform_create(serializer)
            return Response({'success': True})
        return Response({'success': False})

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        is_deleted = instance.delete()
        if is_deleted:
            return Response({'success': True})
        return Response({'success': False})


class FavoriteApiView(BaseInstanceView):
    queryset = Favorite.objects.all()
    serializer_class = FavoriteSerializer

    def get_object(self):
        queryset = self.filter_queryset(self.get_queryset())
        instance = get_object_or_404(
            queryset,
            user=self.request.user,
            recipe=self.kwargs['pk'],
        )
        self.check_object_permissions(self.request, instance)
        return instance


class FollowApiView(BaseInstanceView):
    queryset = Follow.objects.all()
    serializer_class = FollowSerializer

    def get_object(self):
        queryset = self.filter_queryset(self.get_queryset())
        instance = get_object_or_404(
            queryset,
            user=self.request.user,
            author=self.kwargs['pk'],
        )
        self.check_object_permissions(self.request, instance)
        return instance
