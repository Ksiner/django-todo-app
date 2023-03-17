from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Snippet


class UserSerializer(serializers.HyperlinkedModelSerializer):
    snippets = serializers.HyperlinkedIdentityField(many=True, read_only=True, view_name="snippet-detail")

    class Meta:
        model = User
        fields = ["url", "id", "username", "snippets"]


class SnippetSerializer(serializers.HyperlinkedModelSerializer):
    # owner = serializers.PrimaryKeyRelatedField(read_only=True)
    owner = UserSerializer(read_only=True)
    highlight = serializers.HyperlinkedIdentityField(view_name="snippet-highlight", format="html")

    class Meta:
        model = Snippet
        fields = ["url", "id", "title", "code", "linenos", "language", "style", "owner", "highlight"]
