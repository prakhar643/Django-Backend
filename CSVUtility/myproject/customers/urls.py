from django.urls import path
from .views import import_customers

urlpatterns = [
    path('import/', import_customers, name='import_customers'),
]