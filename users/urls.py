from django.urls import path
from users.views import UserRegisterView
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

app_name = "users"

urlpatterns = [
    path("/register", UserRegisterView.as_view(), name="register"),
    path("/login", TokenObtainPairView.as_view(), name="login"),
    path("/refresh", TokenRefreshView.as_view(), name="refresh-token"),
]
