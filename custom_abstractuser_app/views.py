from django.shortcuts import render
from django.views.generic.edit import CreateView
from django.urls import reverse_lazy
from django.contrib import messages

from custom_abstractuser_app.forms import CustomUserCreationForm

class CustomUserCreateView(CreateView):
    form_class = CustomUserCreationForm
    template_name = 'custom_abstractuser_app/register.html'
    success_url = reverse_lazy('success')
    def post(self, request, *args, **kwargs):
        messages.success(request, f'Account created successfully')
        return super().post(request, *args, **kwargs)