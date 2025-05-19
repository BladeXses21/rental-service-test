from rest_framework import serializers
from apps.apartments.models import Apartment

class ApartmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Apartment
        fields = '__all__'
        read_only_fields = ('owner', 'created_at', 'updated_at')
