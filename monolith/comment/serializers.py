from rest_framework.serializers import ModelSerializer
from comment import models


class CommentListSerializer(ModelSerializer):
    class Meta:
        model = models.Comment
        fields = ('course', 'plan')


class CommentSerializer(ModelSerializer):
    class Meta:
        model = models.Comment
        fields = '__all__'
