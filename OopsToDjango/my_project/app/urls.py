from django.urls import path
from .views import HelloApiView,ApiProducts

urlpatterns = [
    path('hello/',HelloApiView.as_view()),
    path('products/',ApiProducts.as_view()),
]