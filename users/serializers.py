from rest_framework import serializers
from users.models import UserModel


class PublicUserInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserModel
        fields = ["id", "name", "email"]


class UserRegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserModel
        fields = ["id", "email", "name", "password"]
        extra_kwargs = {
            "password": {"write_only": True},
        }

    def create(self, validated_data):
        print(validated_data)
        user = UserModel.objects.create(email=validated_data["email"], name=validated_data["name"])
        user.set_password(validated_data["password"])
        user.save()

        return user
