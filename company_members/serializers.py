from rest_framework import serializers
from company_members.models import CompanyMemberModel
from users.models import UserModel


class CompanyMemberUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserModel
        fields = ["id", "name", "email"]


class CompanyMemberSerializer(serializers.ModelSerializer):
    user = CompanyMemberUserSerializer(read_only=True)

    class Meta:
        model = CompanyMemberModel
        fields = [
            "id",
            "role",
            "user",
        ]
