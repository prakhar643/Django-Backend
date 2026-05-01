from django.db import models
from rest_framework.serializers import ModelSerializer

# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length=100)
    price= models.IntegerField()
