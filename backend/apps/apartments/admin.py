from django.contrib import admin
from .models import Apartment

@admin.register(Apartment)
class ApartmentAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'availability', 'owner', 'created_at')
    list_filter = ('availability', 'number_of_rooms')
    search_fields = ('name', 'description', 'slug')
    prepopulated_fields = {'slug': ('name',)}
