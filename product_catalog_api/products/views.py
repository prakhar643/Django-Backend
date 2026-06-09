from .models import Order, OrderItem
from .serializer import OrderSerializer, OrderItemSerializer
from rest_framework.views import APIView
from rest_framework.response import Response


class OrderCreateAPIView(APIView):

    def get(self,request):
        order = Order.objects.all()
        serializer = OrderSerializer(order,many = True)
        return Response(serializer.data)


    def post(self, request):
        serializer = OrderSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response(serializer.data)