from django.contrib import admin
from common.models import MediaFile


@admin.register(MediaFile)
class MediaFileAdmin(admin.ModelAdmin):
    list_display = ('file', 'car')
    search_fields = ('file', 'car__name')
    ordering = ('-created_at',)
    list_per_page = 10
    date_hierarchy = 'created_at'