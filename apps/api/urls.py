from rest_framework.routers import DefaultRouter

from apps.api import views

router = DefaultRouter()
router.register('v1/favorites', views.FavoriteApiView)
router.register('v1/subscriptions', views.FollowApiView)
router.register('v1/purchases', views.PurchaseApiView)
router.register('v1/ingredients', views.IgredientApiView)

urlpatterns = router.urls
