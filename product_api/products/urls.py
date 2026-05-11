from django.urls import path,include
# from .views import Product_View,ProductDetailView 
# from rest_framework.routers import DefaultRouter  
from rest_framework.routers import DefaultRouter
from .views import ProductViewSet        

# urlpatterns = [
#     path('products/',Product_View.as_view() ),
#     path('products/<int:pk>',ProductDetailView.as_view() ),
# ]

router = DefaultRouter()
router.register('products',ProductViewSet,basename='product')


urlpatterns = [
    path('', include(router.urls)),
]