from rest_framework import viewsets, permissions
from apps.apartments.models import Apartment
from .serializers import ApartmentSerializer
from apps.apartments.filters import ApartmentFilter
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter
from rest_framework.pagination import PageNumberPagination
from apps.apartments.api.permissions import IsOwnerPermission

class ApartmentViewSet(viewsets.ModelViewSet):
    queryset = Apartment.objects.all()
    serializer_class = ApartmentSerializer
    lookup_field = 'slug'
    filter_backends = [DjangoFilterBackend]
    filterset_class = ApartmentFilter
    pagination_class = PageNumberPagination

    def get_permissions(self):
        if self.action in ['list', 'retrieve']:
            permission_classes = [permissions.AllowAny]
        elif self.action in ['create']:
            permission_classes = [permissions.IsAuthenticated]
        else:  # update, partial_update, destroy
            permission_classes = [permissions.IsAuthenticated, IsOwnerPermission]
        return [permission() for permission in permission_classes]

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)
