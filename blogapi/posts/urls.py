from .views import BlogApiView
from django.urls import path

urlpatterns = [
    path('posts/',BlogApiView.as_view(), name='blog-list-create' ),
    path('posts/<int:pk>/', BlogApiView.as_view()),
]