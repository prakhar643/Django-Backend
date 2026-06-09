from django.shortcuts import render, get_object_or_404
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response

from rest_framework.permissions import IsAuthenticated
from .models import UserPlan
from .serializers import UserPlanSerializer
from rest_framework.decorators import throttle_classes
from .throttles import PlanBasedThrottle

# Create your views here.
@api_view(['GET'])
def home(request):
    return Response({
        "message" : "SaaS API running"
    })


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def my_plan(request):

    user_plan = get_object_or_404(UserPlan, user=request.user)

    serializer = UserPlanSerializer(user_plan)

    return Response(serializer.data)


@api_view(['GET'])
@permission_classes([IsAuthenticated])
@throttle_classes([PlanBasedThrottle])
def limited_api(request):

    return Response({
        "message": "Request successful"
    })