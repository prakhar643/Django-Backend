from .models import Product
from rest_framework.serializers import ModelSerializer

# Create your models here.
class ProductSerializer(ModelSerializer):
    class Meta:
        model = Product
        fields = ["name","price"]

    def validate_price(self,value):
        if value <= 0:
            raise ValueError("Price must be greater than 0")
        return value
    
    def validate(self,data):
        if not data.get("name"):
            raise ValueError("Name cannot be empty")
        return data