from pyexpat import model
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser
from .forms import CustomUserCreationForm, CustomUserChangeForm


@admin.register(CustomUser)
class CustomUserAdmin(UserAdmin):
    model = CustomUser
    form = CustomUserChangeForm
    add_form = CustomUserCreationForm
    list_display = UserAdmin.list_display + ("age", )
    fieldsets = UserAdmin.fieldsets + (
        (None, {"fields": ("age",)}),
    )
    add_fieldsets = UserAdmin.fieldsets + (
        (None, {"fields": ("age",)}),
    )

