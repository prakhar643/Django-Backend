from rest_framework import serializers
from .models import BlogApiModel
from django.contrib.auth.models import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username' ]

class BlogSerializer(serializers.ModelSerializer):
    author = UserSerializer(read_only = True)

    class Meta:
        model = BlogApiModel
        fields = '__all__'
        read_only_fields = ['created_at', 'updated_at']