from rest_framework import generics
from companies.models import CompanyModel
from companies.serializers import CompanySerializer


class CreateListCompanyView(generics.ListCreateAPIView):
    serializer_class = CompanySerializer

    def get_queryset(self):
        user = self.request.user

        return (
            CompanyModel.objects.prefetch_related("companymembermodel").all().filter(companymembermodel__user=user.id)
        )
