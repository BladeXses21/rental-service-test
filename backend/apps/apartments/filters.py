from django_filters import rest_framework as filters
from .models import Apartment
from django.db.models import Q

class ApartmentFilter(filters.FilterSet):
    price_min = filters.NumberFilter(field_name="price", lookup_expr='gte')
    price_max = filters.NumberFilter(field_name="price", lookup_expr='lte')
    rooms = filters.NumberFilter(field_name="number_of_rooms")
    available = filters.BooleanFilter(field_name="availability")
    search = filters.CharFilter(method='filter_search')

    class Meta:
        model = Apartment
        fields = ['price_min', 'price_max', 'rooms', 'available', 'search']

    def filter_search(self, queryset, name, value):
        return queryset.filter(
            Q(name__icontains=value) | Q(description__icontains=value)
        )
