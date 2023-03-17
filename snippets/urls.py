from django.urls import path, include
from rest_framework.routers import DefaultRouter
from snippets import views
from rest_framework.urlpatterns import format_suffix_patterns

# app_name = "snippets"

# snippet_list = views.SnippetViewSet.as_view({"get": "list", "post": "create"})
# snippet_detail = views.SnippetViewSet.as_view(
#     {"get": "retrieve", "put": "update", "patch": "partial_update", "delete": "destroy"}
# )
# snippet_highlighter = views.SnippetViewSet.as_view(
#     {
#         "get": "highlight",
#     }
# )
# user_list = views.UserViewSet.as_view(
#     {
#         "get": "list",
#     }
# )
# user_detail = views.UserViewSet.as_view(
#     {
#         "get": "retrieve",
#     }
# )

router = DefaultRouter()
router.register(r"snippets", viewset=views.SnippetViewSet, basename="snippet")
router.register(r"users", viewset=views.UserViewSet, basename="user")

urlpatterns = [
    path("", include(router.urls)),
    # path("", view=views.api_root),
    # path("users/", user_list, name="user-list"),
    # path("users/<int:pk>/", user_detail, name="user-detail"),
    # path("snippets/", snippet_list, name="snippet-list"),
    # path("snippets/<int:pk>/", snippet_detail, name="snippet-detail"),
    # path("snippets/<int:pk>/highlight/", snippet_highlighter, name="snippet-highlight"),
]
