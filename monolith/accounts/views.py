from rest_framework import generics
from accounts.models import Account
from .serializers import MyTokenObtainPairSerializer, PostCreateSerializer, ShowMyInformationsSerializer
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework.views import APIView


class MyObtainTokenPairView(TokenObtainPairView):
    permission_classes = (AllowAny,)
    serializer_class = MyTokenObtainPairSerializer


class PostCreateAPIView(generics.CreateAPIView):
    queryset = Account.objects.all()
    serializer_class = PostCreateSerializer


class GetMyInformation(generics.ListAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = ShowMyInformationsSerializer

    def get_queryset(self, *args, **kwargs):
        return Account.objects.filter(id=self.request.user)
