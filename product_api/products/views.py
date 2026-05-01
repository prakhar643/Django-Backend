from django.shortcuts import render
from .models import Product
from .serializers import ProductSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.generics import ListCreateAPIView,RetrieveUpdateDestroyAPIView
from rest_framework.viewsets import ModelViewSet


class ProductViewSet(ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer




# class Product_View(ListCreateAPIView):
#     queryset = Product.objects.all()
#     serializer_class = ProductSerializer


# class ProductDetailView(RetrieveUpdateDestroyAPIView):
#     queryset = Product.objects.all()
#     serializer_class = ProductSerializer

    # def get(self,request):
    #     data = self.get_queryset()
    #     serializer = self.get_serializer(data,many = True)
    #     return Response(serializer.data)

    # def post(self,request):
    #     serializer = self.get_serializer(data=request.data)

    #     if serializer.is_valid():
    #         serializer.save()
    #         return Response(serializer.data, status=status.HTTP_201_CREATED)
        
    #     return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    # def get(self, request):
    #     products = Product.objects.all()
    #     serializer = ProductSerializer(products, many=True)
    #     return Response(serializer.data)
    

    # def post(self, request):
    #     serializer = ProductSerializer(data=request.data)

    #     if serializer.is_valid():
    #         serializer.save()
    #         return Response(serializer.data, status=status.HTTP_201_CREATED)
        
    #     return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)