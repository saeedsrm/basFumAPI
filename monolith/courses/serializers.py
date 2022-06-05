from rest_framework.serializers import ModelSerializer
from courses import models


# course
class CourseListSerializer(ModelSerializer):
    class Meta:
        model = models.Courses
        fields = '__all__'


class CourseDetailSerializer(ModelSerializer):
    class Meta:
        model = models.Courses
        fields = '__all__'


class CourseUpdateSerializer(ModelSerializer):
    class Meta:
        model = models.Courses
        fields = '__all__'


class CourseCreateSerializer(ModelSerializer):
    class Meta:
        model = models.Courses
        fields = '__all__'


class CourseDeleteSerializer(ModelSerializer):
    class Meta:
        model = models.Courses
        fields = '__all__'


# end course

class UserCourseSerializer(ModelSerializer):
    class Meta:
        model = models.User_Course
        fields = '__all__'

