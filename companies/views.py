from rest_framework import generics
from companies.models import CompanyModel
from companies.serializers import CompanySerializer
from rest_framework_simplejwt.authentication import JWTAuthentication


class CreateListCompanyView(generics.ListCreateAPIView):
    serializer_class = CompanySerializer
    authentication_classes = [JWTAuthentication]

    def get_queryset(self):
        user = self.request.user

        return CompanyModel.objects.all().filter(members__user=user.id)

    def perform_create(self, serializer: CompanySerializer):
        serializer.save(creator=self.request.user.id)
