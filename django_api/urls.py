"""django_api URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import include, path
from rest_framework.schemas import get_schema_view
from django.views.generic import TemplateView
from rest_framework import permissions
from rest_framework_simplejwt.authentication import JWTAuthentication
from drf_spectacular.views import SpectacularAPIView, SpectacularRedocView, SpectacularSwaggerView

urlpatterns = [
    path("admin", admin.site.urls),
    path("users", include("users.urls")),
    path("companies", include("companies.urls")),
    # path("polls", include("polls.urls")),
    # path("", include("snippets.urls")),
    # path("api-auth/", include("rest_framework.urls", namespace="rest_framework")),
    path("reference/openapi/api", SpectacularAPIView.as_view(), name="schema"),
    path("reference/openapi/ui", SpectacularSwaggerView.as_view(url_name="schema"), name="swagger-ui"),
]
