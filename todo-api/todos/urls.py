
from django.urls import path,include
from .views import TodoViewSet
from rest_framework.routers import DefaultRouter
from todos.views import LogoutView

router = DefaultRouter()
router.register('todo',TodoViewSet,basename='todo')

urlpatterns = [
    path('', include(router.urls) ),
    path('logout/', LogoutView.as_view(), name='logout'),
]
