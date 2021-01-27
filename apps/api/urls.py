from rest_framework.routers import DefaultRouter

from apps.api.views import FavoriteApiView, FollowApiView

router = DefaultRouter()
router.register('v1/favorites', FavoriteApiView)
router.register('v1/subscriptions', FollowApiView)

urlpatterns = router.urls
