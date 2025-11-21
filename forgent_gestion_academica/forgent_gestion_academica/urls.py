from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views
from gestion_academica.views import custom_logout 

urlpatterns = [
    path("admin/", admin.site.urls),

    # Autenticación
    path("accounts/login/", auth_views.LoginView.as_view(
        template_name="registration/login.html"), name="login"),
    path("accounts/logout/", custom_logout, name="logout"),

    # App principal
    path("", include("gestion_academica.urls")),
]