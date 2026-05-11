from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response

# Create your views here.
class HelloApiView(APIView):
    def get(self,request):
        return Response({"message" : "Hello API"})



class ApiProducts(APIView):
    def get(self,request):
        data = ["apple", "banana", "mango"]
        return Response(data)