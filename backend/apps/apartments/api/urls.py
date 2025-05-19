from django.urls import path, include
from rest_framework.routers import DefaultRouter
from apps.apartments.api.views import ApartmentViewSet

router = DefaultRouter()
router.register(r'apartments', ApartmentViewSet, basename='apartment')

urlpatterns = [
    path('api/v1/', include(router.urls)),
]
