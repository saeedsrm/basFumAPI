from rest_framework import generics

from courses import models
from rest_framework.permissions import (
    IsAuthenticated,
)

from courses.serializers import (
    CourseListSerializer,
    CourseDetailSerializer,
    UserCourseSerializer,
    ChapterSerializer
)
from rest_framework import filters


class CoursesPostListAPIView(generics.ListAPIView):
    queryset = models.Courses.objects.filter(isfinish=False)
    serializer_class = CourseListSerializer
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    ordering_fields = ['name', 'cost', 'date']
    search_fields = ['name', 'date']


class CoursesPostDetailAPIView(generics.RetrieveAPIView):
    queryset = models.Courses.objects.all()
    serializer_class = CourseDetailSerializer
    lookup_field = 'id'
    permission_classes = [IsAuthenticated]


# class ListChapterOfCourseAPIView(generics.ListAPIView):
#     serializer_class = ChapterSerializer
#     permission_classes = [IsAuthenticated]
#
#     def get_queryset(self, *args, **kwargs):
#         return models.Chapter.objects.filter(user=self.request.user)


class UserCourseCreateAPIView(generics.CreateAPIView):
    queryset = models.User_Course.objects.all()
    serializer_class = UserCourseSerializer
    permission_classes = [IsAuthenticated]


class ListMyCoursesAPIView(generics.ListAPIView):
    serializer_class = UserCourseSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self, *args, **kwargs):
        return models.User_Course.objects.filter(user=self.request.user)

# class CoursesPostUpdateAPIView(generics.UpdateAPIView):
#     queryset = models.Courses.objects.all()
#     serializer_class = CourseUpdateSerializer
#     lookup_field = 'id'
#     permission_classes = [IsAuthenticated]
#
#
# class CoursesPostCreateAPIView(generics.CreateAPIView):
#     queryset = models.Courses.objects.all()
#     serializer_class = CourseCreateSerializer
#     permission_classes = [IsAuthenticated]
#
#
# class CoursesPostDeleteAPIView(generics.DestroyAPIView):
#     queryset = models.Courses.objects.all()
#     serializer_class = CourseDeleteSerializer
#     lookup_field = 'id'
#     permission_classes = [IsAuthenticated]
