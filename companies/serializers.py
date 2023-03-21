from rest_framework import serializers
from companies.models import CompanyModel
from company_members.serializers import CompanyMemberSerializer
from company_members.models import CompanyMemberRoles, CompanyMemberModel
from django.utils import timezone
import copy


class CompanySerializer(serializers.ModelSerializer):
    creator = serializers.IntegerField(write_only=True)
    members = CompanyMemberSerializer(many=True, read_only=True)

    class Meta:
        model = CompanyModel
        fields = ["id", "name", "members", "creator"]

    def create(self, validated_data):
        validated_data_copy = copy.deepcopy(validated_data)
        creator_id = validated_data_copy.pop("creator")

        company = CompanyModel.objects.create(**validated_data_copy)
        CompanyMemberModel.objects.create(
            user_id=creator_id, role=CompanyMemberRoles.ADMIN.value, joined_at=timezone.now(), company_id=company.id
        )

        return company
