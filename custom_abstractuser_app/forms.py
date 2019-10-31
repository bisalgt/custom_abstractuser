from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django import forms
from django.conf import settings

from custom_abstractuser_app.models import CustomUser


class CustomUserCreationForm(UserCreationForm):
    
    class Meta:
        model = CustomUser
        fields = ('username', 'first_name', 'last_name', 'email', 'address', 'contact_number')
    

class CustomUserChangeForm(UserChangeForm):
    
    class Meta:
        model = CustomUser
        fields = ('first_name', 'last_name', 'email', 'address', 'contact_number')
