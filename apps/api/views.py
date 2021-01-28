import types

from django.shortcuts import get_object_or_404
from rest_framework import mixins, viewsets
from rest_framework.response import Response

from apps.api.serializer import (
    FavoriteSerializer,
    FollowSerializer,
    PurchaseSerializer,
)
from apps.recipes.models import Favorite, Follow, Purchase

_SUCCESS_RESPONSE = types.MappingProxyType({'success': True})
_UNSUCCESS_RESPONSE = types.MappingProxyType({'success': False})


class BaseInstanceView(
    mixins.CreateModelMixin,
    mixins.DestroyModelMixin,
    viewsets.GenericViewSet,
):
    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            self.perform_create(serializer)
            return Response(_SUCCESS_RESPONSE)
        return Response(_UNSUCCESS_RESPONSE)

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        is_deleted = instance.delete()
        if is_deleted:
            return Response(_SUCCESS_RESPONSE)
        return Response(_UNSUCCESS_RESPONSE)


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


class PurchaseApiView(mixins.ListModelMixin, BaseInstanceView):
    queryset = Purchase.objects.all()
    serializer_class = PurchaseSerializer

    def get_object(self):
        queryset = self.filter_queryset(self.get_queryset())
        instance = get_object_or_404(
            queryset,
            user=self.request.user,
            recipe=self.kwargs['pk'],
        )
        self.check_object_permissions(self.request, instance)
        return instance
