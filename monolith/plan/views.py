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
    PostListSerializer,
    PostDetailSerializer,
    PostUpdateSerializer,
    PostCreateSerializer,
    PostDeleteSerializer
)
from rest_framework import filters


class PlanPostListAPIView(generics.ListAPIView):
    queryset = models.Plan.objects.filter(is_finish=False)
    serializer_class = PostListSerializer
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    ordering_fields = ['name', 'cost', 'date']
    search_fields = ['name', 'date']
    # def get_queryset(self,*args,**kwargs):
    #     return Article.objects.all()


class PlanPostDetailAPIView(generics.RetrieveAPIView):
    queryset = models.Plan.objects.all()
    serializer_class = PostDetailSerializer
    lookup_field = 'id'
    permission_classes = [IsAuthenticated]


class PlanPostUpdateAPIView(generics.UpdateAPIView):
    queryset = models.Plan.objects.all()
    serializer_class = PostUpdateSerializer
    lookup_field = 'id'
    permission_classes = [IsAuthenticated]


class PlanPostCreateAPIView(generics.CreateAPIView):
    queryset = models.Plan.objects.all()
    serializer_class = PostCreateSerializer
    permission_classes = [IsAuthenticated]


class PlanPostDeleteAPIView(generics.DestroyAPIView):
    queryset = models.Plan.objects.all()
    serializer_class = PostDeleteSerializer
    lookup_field = 'id'
    permission_classes = [IsAuthenticated]
