from django.shortcuts import render

from rest_framework import generics, status
from rest_framework.views import APIView
from plan import models
from rest_framework.permissions import (
    AllowAny,
    IsAuthenticated,
    IsAdminUser,
)
from rest_framework.response import Response
from plan.serializers import (
    PlanListSerializer,
    PlanDetailSerializer,
    User_PlanSerializer
)
from rest_framework import filters
from django.contrib.auth import logout
from django.shortcuts import redirect


class PlanPostListAPIView(generics.ListAPIView):
    queryset = models.Plan.objects.filter(is_finish=False)
    serializer_class = PlanListSerializer
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    ordering_fields = ['name', 'cost', 'date']
    search_fields = ['name', 'date']
    # def get_queryset(self,*args,**kwargs):
    #     return Article.objects.all()


class PlanPostDetailAPIView(generics.RetrieveAPIView):
    queryset = models.Plan.objects.all()
    serializer_class = PlanDetailSerializer
    lookup_field = 'id'
    permission_classes = [IsAuthenticated]


class UserPlanCreateAPIView(generics.CreateAPIView):
    queryset = models.User_Plan.objects.all()
    serializer_class = User_PlanSerializer
    permission_classes = [IsAuthenticated]


class ListMyPlanAPIView(generics.ListAPIView):
    serializer_class = User_PlanSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self, *args, **kwargs):
        return models.User_Plan.objects.filter(user=self.request.user)


def logout_view(request):
    logout(request)
    return redirect('/')
