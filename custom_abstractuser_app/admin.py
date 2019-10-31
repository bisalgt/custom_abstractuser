from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from custom_abstractuser_app.forms import CustomUserCreationForm, CustomUserChangeForm
from custom_abstractuser_app.models import CustomUser


class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = CustomUser
    list_display = ('username', 'email', 'first_name', 'last_name', 'address', 'contact_number')

admin.site.register(CustomUser, CustomUserAdmin)