from rest_framework import serializers
from companies.models import CompanyModel
from company_members.serializers import CompanyMemberSerializer
from company_members.models import CompanyMemberRoles, CompanyMemberModel
from django.utils import timezone
from drf_spectacular.utils import extend_schema_field
import copy


class CompanySerializer(serializers.ModelSerializer):
    creator = serializers.HiddenField(default=None)

    class Meta:
        model = CompanyModel
        fields = ["id", "name", "creator"]

    def create(self, validated_data):
        validated_data_copy = copy.deepcopy(validated_data)
        creator_id = validated_data_copy.pop("creator")

        company = CompanyModel.objects.create(**validated_data_copy)
        company.members.add(
            CompanyMemberModel(
                user_id=creator_id, role=CompanyMemberRoles.ADMIN.value, joined_at=timezone.now(), company_id=company.id
            ),
            bulk=False,
        )

        return company
