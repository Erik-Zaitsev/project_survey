from rest_framework import generics, views
from rest_framework.response import Response
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
    serializer_class = CustomUserSerializer
    permission_classes = (IsSuperuserPermission, )
    pagination_class = APIViewPagination
    
    def get(self, request, pk):
        queryset = CustomUser.objects.get(pk=pk)
        return Response(
            {'result': CustomUserSerializer(queryset).data}
        )
        
    def post(self, request):
        serializer = CustomUserSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({'result': serializer.data})