from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework_simplejwt.exceptions import TokenError

from .models import Todo
from .serializers import TodoSerializer
from .permissions import IsOwner


# ✅ Todo CRUD API (JWT Protected)
class TodoViewSet(ModelViewSet):
    def get_queryset(self):
        return Todo.objects.filter(owner=self.request.user)
    serializer_class = TodoSerializer
    permission_classes = [IsAuthenticated,IsOwner]

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


# 🔐 Logout API (Blacklist refresh token)
class LogoutView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        refresh_token = request.data.get("refresh")
        if not refresh_token:
            return Response(
                {"error": "Refresh token is required."},
                status=status.HTTP_400_BAD_REQUEST,
            )

        try:
            token = RefreshToken(refresh_token)
            token.blacklist()

            return Response(
                {"message": "Logged out successfully"},
                status=status.HTTP_200_OK,
            )

        except TokenError as e:
            return Response(
                {"error": "Invalid token", "details": str(e)},
                status=status.HTTP_400_BAD_REQUEST,
            )