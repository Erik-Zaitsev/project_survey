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
    
    def get(self, request, pk):
        if not pk:
            return Response({'result': 'Добавьте к URL id записи!'})
        
        try:
            instance = CustomUser.objects.get(pk=pk)
        except:
            return Response({'result': 'Объект с данным id не найден!'})
            
        return Response({'result': CustomUserSerializer(instance).data})
        
        
    def post(self, request):
        serializer = CustomUserSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({'result': serializer.data})
    
    
    def delete(self, request, pk):
        if not pk:
            return Response({'result': 'Добавьте к URL id записи!'})
        
        try:
            instance = CustomUser.object.get(pk=pk)
        except:
            return Response({'result': 'Объект с данным id не найден!'})
        
        CustomUser.objects.get(pk=pk).delete()
        return Response({'result': 'Объект удалён!'})
        