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


# end plan

class User_PlanSerializer(ModelSerializer):
    class Meta:
        model = models.User_Plan
        fields = '__all__'
