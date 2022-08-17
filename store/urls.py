from django.urls import path, include
from .views import StoreViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter(trailing_slash=False)


router.register("", StoreViewSet, basename="store")

urlpatterns = router.urls
