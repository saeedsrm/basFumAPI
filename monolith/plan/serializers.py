from rest_framework.serializers import ModelSerializer
from plan import models


# plan
class PlanListSerializer(ModelSerializer):
    class Meta:
        model = models.Plan
        fields = '__all__'


class PlanDetailSerializer(ModelSerializer):
    class Meta:
        model = models.Plan
        fields = '__all__'


class PlanUpdateSerializer(ModelSerializer):
    class Meta:
        model = models.Plan
        fields = '__all__'


class PlanCreateSerializer(ModelSerializer):
    class Meta:
        model = models.Plan
        fields = '__all__'


class PlanDeleteSerializer(ModelSerializer):
    class Meta:
        model = models.Plan
        fields = '__all__'


# end plan

class User_PlanCreateSerializer(ModelSerializer):
    class Meta:
        model = models.User_Plan
        fields = '__all__'
