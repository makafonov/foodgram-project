from rest_framework.routers import DefaultRouter

from apps.api.views import FavoriteApiView

router = DefaultRouter()
router.register('v1/favorites', FavoriteApiView)

urlpatterns = router.urls
