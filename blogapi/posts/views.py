from django.shortcuts import render
from rest_framework.views import APIView
from .models import BlogApiModel
from .serializers import BlogSerializer
from rest_framework.response import Response
from rest_framework import status
from .permission import IsAuthor
from django.shortcuts import get_object_or_404
# Create your views here.

class BlogApiView(APIView):
    def get(self,request):
        post = BlogApiModel.objects.all()
        serializer = BlogSerializer(post,many=True)

        return Response(serializer.data)


    def post(self, request):
        serializer = BlogSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save(author=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
    
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


    def put(self,request):
        post_id = request.data.get('id')
        post = get_object_or_404(BlogApiModel, id=post_id)
        self.check_object_permissions(request, post)
        serializer = BlogSerializer(post, data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


    def delete(self, request, pk):
        post = get_object_or_404(BlogApiModel, pk=pk)

        self.check_object_permissions(request, post)

        post.delete()

        return Response(status=status.HTTP_204_NO_CONTENT)