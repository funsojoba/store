from django.urls import path, include
from .views import OrderViewset, ItemViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter(trailing_slash=False)


router.register(r"store", OrderViewset, basename="order")
router.register(r"order", ItemViewSet, basename="item")

urlpatterns = router.urls
