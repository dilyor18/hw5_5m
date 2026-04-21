from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import OrderViewSet

from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

router = DefaultRouter()
router.register('orders', OrderViewSet)

schema_view = get_schema_view(
    openapi.Info(
        title="API",
        default_version='v1',
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    path('', include(router.urls)),  # ← ВОТ ЭТО ТЫ ЗАБЫЛ

    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0)),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0)),
]
