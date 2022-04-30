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

import threading


class PostListAPIView(generics.ListAPIView):
    queryset = models.Plan.objects.all()
    serializer_class = PostListSerializer
    permission_classes = [IsAuthenticated]
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    ordering_fields = ['name', 'cost', 'date']
    search_fields = ['name', 'date']
    # def get_queryset(self,*args,**kwargs):
    #     return Article.objects.all()


class PostDetailAPIView(generics.RetrieveAPIView):
    queryset = models.Plan.objects.all()
    serializer_class = PostDetailSerializer
    lookup_field = 'id'
    permission_classes = [IsAuthenticated]


class PostUpdateAPIView(generics.UpdateAPIView):
    queryset = models.Plan.objects.all()
    serializer_class = PostUpdateSerializer
    lookup_field = 'id'
    permission_classes = [IsAuthenticated]


class PostCreateAPIView(generics.CreateAPIView):
    queryset = models.Plan.objects.all()
    serializer_class = PostCreateSerializer
    permission_classes = [IsAuthenticated]


class PostDeleteAPIView(generics.DestroyAPIView):
    queryset = models.Plan.objects.all()
    serializer_class = PostUpdateSerializer
    lookup_field = 'id'
    permission_classes = [IsAuthenticated]
