from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User


@admin.register(User)
class CustomUserAdmin(UserAdmin):
    model = User
    list_display = ('username', 'email', 'is_active', 'is_verified', 'is_staff')
    list_filter = ('is_active', 'is_verified', 'is_staff')
