from django.contrib import admin
from users.models import CustomUser

@admin.register(CustomUser)
class CustomUserAdmin(admin.ModelAdmin):
    list_display = ('id','username', 'email', 'first_name', 'last_name', 'is_staff', 'is_active','is_superuser')
    list_display_links = ('username', 'email','first_name', 'last_name','is_staff')
    search_fields = ('id','username', 'email', 'first_name', 'last_name')
    list_filter = ('is_staff', 'is_active')
    ordering = ('-date_joined',)
    list_per_page = 10
    date_hierarchy = 'date_joined'
    fieldsets = (
        (None, {
            'fields': ('username', 'email', 'password')
        }),
        ('Personal info', {
            'fields': ('first_name', 'last_name', 'avatar', 'profession', 'bio','comments')
        }),
        ('Permissions', {
            'fields': ('is_active', 'is_staff', 'is_superuser' ,  'groups', 'user_permissions')
        }),
        ('Important dates', {
            'fields': ('last_login',)
        }),
    )   

