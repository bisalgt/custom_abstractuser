from django.contrib.auth.views import LoginView, LogoutView, TemplateView
from django.urls import path

from custom_abstractuser_app import views

urlpatterns = [
    path('register/', views.CustomUserCreateView.as_view(), name='register' ),
    path('success/', TemplateView.as_view(template_name='custom_abstractuser_app/success.html'), name='success' ),
    path("login/", LoginView.as_view(template_name='custom_abstractuser_app/login.html'), name="login"),
    path("logout/", LogoutView.as_view(template_name='custom_abstractuser_app/logout.html'), name="logout"),
]
