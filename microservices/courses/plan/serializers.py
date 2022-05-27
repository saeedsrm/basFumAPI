from rest_framework.serializers import ModelSerializer
from plan import models

# plan
class PostListSerializer(ModelSerializer):
    class Meta:
        model = models.Plan
        fields = '__all__'


class PostDetailSerializer(ModelSerializer):
    class Meta:
        model = models.Plan
        fields = '__all__'


class PostUpdateSerializer(ModelSerializer):
    class Meta:
        model = models.Plan
        fields = '__all__'


class PostCreateSerializer(ModelSerializer):
    class Meta:
        model = models.Plan
        fields = '__all__'


class PostDeleteSerializer(ModelSerializer):
    class Meta:
        model=models.Plan
        fields='__all__'

# end plan