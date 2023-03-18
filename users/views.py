from rest_framework import generics
from rest_framework.response import Response
from users.serializers import UserRegisterSerializer
from users.models import UserModel


class UserRegisterView(generics.GenericAPIView):
    queryset = UserModel.objects.all()
    serializer_class = UserRegisterSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response(serializer.data)
