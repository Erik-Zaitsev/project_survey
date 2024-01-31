from django.urls import path, include
from .views import CustomUserListAPIView, CustomUserAPIView


urlpatterns = [
    path('', CustomUserListAPIView().as_view()),
    path('<int:pk>/', CustomUserAPIView().as_view()),
]
