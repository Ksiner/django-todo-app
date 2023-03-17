from rest_framework import permissions, serializers
from .models import Snippet
from django.contrib.auth.models import User


class IsOwnerOrReadOnly(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True

        return obj.owner == request.user


class UserSerializer(serializers.ModelSerializer):
    snippets = serializers.RelatedField(many=True, queryset=Snippet.objects.all())

    class Meta:
        model = User
        fields = ["id", "username", "snippets"]
