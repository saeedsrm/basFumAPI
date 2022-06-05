from rest_framework import generics

from courses import models
from rest_framework.permissions import (
    IsAuthenticated,
)

from courses.serializers import (
    PostListSerializer,
    PostDetailSerializer,
    PostUpdateSerializer,
    PostCreateSerializer,
    PostDeleteSerializer
)
from rest_framework import filters


class CoursesPostListAPIView(generics.ListAPIView):
    queryset = models.Courses.objects.filter(isfinish=False)
    serializer_class = PostListSerializer
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    ordering_fields = ['name', 'cost', 'date']
    search_fields = ['name', 'date']
    # def get_queryset(self,*args,**kwargs):
    #     return Article.objects.all()
    # permission_classes = [IsAuthenticated]


class CoursesPostDetailAPIView(generics.RetrieveAPIView):
    queryset = models.Courses.objects.all()
    serializer_class = PostDetailSerializer
    lookup_field = 'id'
    permission_classes = [IsAuthenticated]


class CoursesPostUpdateAPIView(generics.UpdateAPIView):
    queryset = models.Courses.objects.all()
    serializer_class = PostUpdateSerializer
    lookup_field = 'id'
    permission_classes = [IsAuthenticated]


class CoursesPostCreateAPIView(generics.CreateAPIView):
    queryset = models.Courses.objects.all()
    serializer_class = PostCreateSerializer
    permission_classes = [IsAuthenticated]


class CoursesPostDeleteAPIView(generics.DestroyAPIView):
    queryset = models.Courses.objects.all()
    serializer_class = PostDeleteSerializer
    lookup_field = 'id'
    permission_classes = [IsAuthenticated]
