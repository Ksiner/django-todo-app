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


urlpatterns = [
    path("admin", admin.site.urls),
    path("users", include("users.urls")),
    path("companies", include("companies.urls")),
    # path("polls", include("polls.urls")),
    # path("", include("snippets.urls")),
    # path("api-auth/", include("rest_framework.urls", namespace="rest_framework")),
    path(
        "reference/openapi/api",
        get_schema_view(
            title="Todos Project",
            description="OpenAPI Schema",
            version="1.0.0",
        ),
        name="openapi-schema",
    ),
    path(
        "reference/openapi/ui",
        TemplateView.as_view(template_name="openapi/swagger-ui.html", extra_context={"schema_url": "openapi-schema"}),
    ),
]
