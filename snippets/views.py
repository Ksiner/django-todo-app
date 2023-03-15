from django.views.decorators.csrf import csrf_exempt
import rest_framework.status as HTTP_STATUSES
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .serializers import SnippetSerializer
from .models import Snippet
from rest_framework import mixins, generics


class SnippetsIndexView(generics.ListCreateAPIView):
    queryset = Snippet.objects.all()
    serializer_class = SnippetSerializer


class SnippetDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Snippet.objects.all()
    serializer_class = SnippetSerializer
