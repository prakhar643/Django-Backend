from rest_framework import serializers
from .models import UserPlan


class UserPlanSerializer(serializers.ModelSerializer):

    username = serializers.CharField(
        source='user.username',
        read_only=True
    )

    class Meta:
        model = UserPlan
        fields = ['username', 'plan']