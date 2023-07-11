from django.shortcuts import render
from .serializers import UserCreateSerializer
from rest_framework.generics import CreateAPIView
from rest_framework.views import APIView
from rest_framework.permissions import IsAdminUser, AllowAny
from .models import User


# Create your views here.

class UserCreateView(CreateAPIView):
    serializer_class = UserCreateSerializer
    permission_classes = [AllowAny, ]

    # queryset = User.objects.all()
    def get_queryset(self):
        return User.objects.all()
