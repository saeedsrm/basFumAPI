from rest_framework import generics
from accounts.models import Account
from .serializers import MyTokenObtainPairSerializer, PostCreateSerializer, ShowMyInformationsSerializer
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework.views import APIView
from rest_framework.response import Response


class MyObtainTokenPairView(TokenObtainPairView):
    permission_classes = (AllowAny,)
    serializer_class = MyTokenObtainPairSerializer


class PostCreateAPIView(generics.CreateAPIView):
    queryset = Account.objects.all()
    serializer_class = PostCreateSerializer


class GetMyInformation(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, *args, **kwargs):
        data=Account.objects.get(email=self.request.user.email)
        ser_data=ShowMyInformationsSerializer(data)
        return Response(ser_data.data)
