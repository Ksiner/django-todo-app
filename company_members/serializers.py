from rest_framework import serializers
from company_members.models import CompanyMemberModel
from users.serializers import PublicUserInfoSerializer


class CompanyMemberSerializer(serializers.ModelSerializer):
    user = PublicUserInfoSerializer(read_only=True)

    class Meta:
        model = CompanyMemberModel
        fields = [
            "id",
            "role",
            "user",
        ]
