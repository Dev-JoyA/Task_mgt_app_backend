# # tasks/urls.py

# from django.urls import path
# from . import views  # Import your views

# urlpatterns = [
#     path('', views.home, name='home'),  # Example route
# ]

from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import TaskViewSet

router = DefaultRouter()
router.register(r'tasks', TaskViewSet)

urlpatterns = [
    path('', include(router.urls)),
]

