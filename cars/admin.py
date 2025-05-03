from django.contrib import admin
from cars.models import Car, Brand

@admin.register(Car)
class CarAdmin(admin.ModelAdmin):
    list_display = ('name', 'brand', 'price', 'year', 'color', 'gear_type', 'distance_covered')
    search_fields = ('name', 'brand__name')
    list_filter = ('brand', 'year', 'gear_type')
    ordering = ('-created_at',)
    list_per_page = 10
    date_hierarchy = 'created_at'


@admin.register(Brand)
class BrandAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)
    ordering = ('-created_at',)
    list_per_page = 10
    date_hierarchy = 'created_at'



