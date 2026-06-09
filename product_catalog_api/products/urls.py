from .views import OrderCreateAPIView
from django.urls import path

urlpatterns = [
    # path('products/', ProductApiView.as_view()),
    path('orders/', OrderCreateAPIView.as_view())
]
