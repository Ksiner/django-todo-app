from rest_framework import generics
from rest_framework.response import Response
from users.serializers import UserRegisterSerializer
from rest_framework_simplejwt.views import TokenRefreshView
from users.models import UserModel
from drf_spectacular.utils import extend_schema, OpenApiParameter, OpenApiExample
from drf_spectacular.types import OpenApiTypes


class UserRegisterView(generics.GenericAPIView):
    queryset = UserModel.objects.all()
    serializer_class = UserRegisterSerializer
    authentication_classes = []

    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response(serializer.data)
