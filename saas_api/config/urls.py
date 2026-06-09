from django.contrib import admin
from django.urls import path
from core.views import home, my_plan ,limited_api

urlpatterns = [
    path('admin/', admin.site.urls),

    path('', home),
    path('my-plan/', my_plan),
    path('limited-api/', limited_api),
]