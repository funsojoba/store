from django.urls import path, include
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static

from rest_framework import permissions

from drf_yasg.views import get_schema_view
from drf_yasg import openapi


schema_view = get_schema_view(
    openapi.Info(
        title="Store API",
        default_version="v1",
        description="e-Commerce store",
    ),
    # validators=["ssv", "flex"],
    public=True,
    permission_classes=[permissions.AllowAny],
)

urlpatterns = [
    path(
        "",
        schema_view.with_ui("swagger", cache_timeout=None),
        name="schema-swagger-ui",
    ),
    path('admin/', admin.site.urls),
    path('api/auth/', include('authentication.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    
