from rest_framework import generics

from monolith.accounts.models import Account
from .serializers import MyTokenObtainPairSerializer, PostCreateSerializer
from rest_framework.permissions import AllowAny
from rest_framework_simplejwt.views import TokenObtainPairView


class MyObtainTokenPairView(TokenObtainPairView):
    permission_classes = (AllowAny,)
    serializer_class = MyTokenObtainPairSerializer


class PostCreateAPIView(generics.CreateAPIView):
    queryset = Account.objects.all()
    serializer_class = PostCreateSerializer
