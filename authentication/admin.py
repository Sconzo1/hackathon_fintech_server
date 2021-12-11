from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .models import User


class CustomUserAdmin(UserAdmin):
    model = User
    list_display = ('full_name', 'phone', 'is_staff', 'is_superuser')
    list_filter = ('is_staff', 'is_superuser', 'birthdate')
    fieldsets = (
        (None, {'fields': ('phone', 'email', 'password')}),
        ('Инфо', {'fields': ('full_name', 'birthdate')}),
        ('Права', {
            'fields': ('is_staff', 'is_superuser', 'groups', 'user_permissions'),
        }),
        ('Данные', {'fields': ('last_login',)}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('phone', 'password1', 'password2', 'is_staff')}
         ),
        (None, {
            'classes': ('wide',),
            'fields': ('phone', 'password1', 'password2'), }),
        ('Инфо', {
            'classes': ('wide',),
            'fields': ('full_name', 'birthdate')}),
        ('Права', {
            'classes': ('wide',),
            'fields': ('is_staff', 'is_superuser', 'groups', 'user_permissions'),
        }),
    )
    readonly_fields = ('last_login',)
    search_fields = ('phone', 'email', 'full_name')
    ordering = ('phone',)


admin.site.register(User, CustomUserAdmin)
