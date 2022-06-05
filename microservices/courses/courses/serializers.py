from rest_framework.serializers import ModelSerializer
from monolith.courses import models


# course
class PostListSerializer(ModelSerializer):
    class Meta:
        model = models.Courses
        fields = '__all__'


class PostDetailSerializer(ModelSerializer):
    class Meta:
        model = models.Courses
        fields = '__all__'


class PostUpdateSerializer(ModelSerializer):
    class Meta:
        model = models.Courses
        fields = '__all__'


class PostCreateSerializer(ModelSerializer):
    class Meta:
        model = models.Courses
        fields = '__all__'


class PostDeleteSerializer(ModelSerializer):
    class Meta:
        model= models.Courses
        fields='__all__'

# end course