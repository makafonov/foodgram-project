from rest_framework.routers import DefaultRouter

from apps.api.views import FavoriteApiView, FollowApiView, PurchaseApiView

router = DefaultRouter()
router.register('v1/favorites', FavoriteApiView)
router.register('v1/subscriptions', FollowApiView)
router.register('v1/purchases', PurchaseApiView)

urlpatterns = router.urls
