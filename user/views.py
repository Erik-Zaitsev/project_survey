from rest_framework import generics, views
from .permissions import IsSuperuserPermission
from .models import CustomUser
from .serializers import CustomUserSerializer
from services import APIViewPagination


# Create your views here.
class CustomUserListAPIView(generics.ListAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = CustomUserSerializer
    permission_classes = (IsSuperuserPermission, )
    pagination_class = APIViewPagination
    
class CustomUserAPIView(views.APIView):
    pass