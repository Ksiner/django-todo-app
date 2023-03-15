from django.urls import path
from .views import SnippetDetailView, SnippetsIndexView
from rest_framework.urlpatterns import format_suffix_patterns

app_name = "snippets"
urlpatterns = [path("", SnippetsIndexView.as_view()), path("/<int:pk>", SnippetDetailView.as_view())]

urlpatterns = format_suffix_patterns(urlpatterns)
