from django.contrib.auth.models import User
from rest_framework import generics, permissions
from oauth2_provider.contrib.rest_framework import TokenHasReadWriteScope, TokenHasScope
from rest_framework.permissions import AllowAny
from drf_spectacular.utils import extend_schema

from .serializers import RegisterSerializer


class RegisterView(generics.CreateAPIView):
    """
    Register a new user.
    """
    queryset = User.objects.all()
    permission_classes = [AllowAny]
    serializer_class = RegisterSerializer
