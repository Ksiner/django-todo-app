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

    def is_user_related_to_company(self, company_id: int, role: CompanyMemberRoles = None):
        count = CompanyMemberModel.objects.filter(
            user_id=self.request.user.id, company_id=company_id, role=role
        ).count()

        if count == 0:
            raise PermissionDenied("You don't have permission to take this action")

        return True

    def can_update(self, company_id: int):
        return self.is_user_related_to_company(company_id=company_id, role=CompanyMemberRoles.ADMIN.value)

    def can_destroy(self, company_id: int):
        return self.is_user_related_to_company(company_id=company_id, role=CompanyMemberRoles.ADMIN.value)

    def perform_update(self, serializer: CompanySerializer):
        if self.can_update(company_id=serializer.instance.id):
            return serializer.save()

    def perform_destroy(self, instance: CompanyModel):
        if self.can_destroy(company_id=instance.id):
            return instance.delete()
