from django.contrib import admin
from .models import Snippet


class SnippetModelAdmin(admin.ModelAdmin):
    list_display = [
        "title",
        "code",
        "linenos",
        "language",
        "style",
        "created_at",
    ]


admin.site.register(Snippet, SnippetModelAdmin)
