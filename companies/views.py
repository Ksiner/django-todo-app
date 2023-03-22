from rest_framework import generics
from companies.models import CompanyModel
from companies.serializers import CompanySerializer
from rest_framework.response import Response
from rest_framework import status
from rest_framework.exceptions import PermissionDenied
from company_members.models import CompanyMemberModel, CompanyMemberRoles


class CreateListCompanyView(generics.ListCreateAPIView):
    serializer_class = CompanySerializer

    def get_queryset(self):
        user = self.request.user

        return CompanyModel.objects.all().filter(members__user=user.id)

    def perform_create(self, serializer: CompanySerializer):
        serializer.save(creator=self.request.user.id)


class RetrieveUpdateDestroyCompanyView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = CompanySerializer

    def get_queryset(self):
        user = self.request.user

        return CompanyModel.objects.all().filter(members__user=user.id)

    def check_object_permissions(self, request, obj):
        # Pass Get requests
        if self.request.method == "GET":
            return

        count = CompanyMemberModel.objects.filter(
            user_id=self.request.user.id, company_id=obj.id, role=CompanyMemberRoles.ADMIN.value
        ).count()

        if count == 0:
            raise PermissionDenied("You don't have permission to take this action")
