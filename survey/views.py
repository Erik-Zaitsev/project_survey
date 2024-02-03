from rest_framework import views, generics
from rest_framework.response import Response
from .models import Survey, Question, Answer
from .serializers import (SurveyListAndGetSerializer, SurveyPostAndPatchSerializer,
                          QuestionListAndGetSerializer, QuestionPostAndPatchSerializer,
                          AnswerListAndGetSerializer, AnswerPostAndPatchSerializer)
from django.forms import model_to_dict
from services import APIViewPagination


# Create your views here.            
class SurveyListAndCreateAPIView(views.APIView):
    def get(self, request, *args, **kwargs):
        queryset = Survey.objects.all()
        return Response({'result': SurveyPostAndPatchSerializer(queryset, many=True).data})
    
    
    def post(self, request, *args, **kwargs):
        serializer = SurveyPostAndPatchSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({'result': serializer.data})
        
        
class SurveyGetPatchDeleteAPIView(views.APIView):
    def get(self, request, *args, **kwargs):
        pk = kwargs.get('pk', None)
        if not pk:
            return Response({'result': 'Добавьте к URL id записи!'})
        
        try:
            instance = Survey.objects.get(pk=pk)
        except:
            return Response({'result': 'Объект с данным id не найден!'})
        
        return Response({'result': SurveyPostAndPatchSerializer(instance).data})
        
        
    def patch(self, request, *args, **kwargs):
        pk = kwargs.get('pk', None)
        if not pk:
            return Response({'result': 'Добавьте к URL id записи!'})
        
        try:
            instance = Survey.objects.get(pk=pk)
        except:
            return Response({'result': 'Объект с данным id не найден!'})
        
        serializer = SurveyPostAndPatchSerializer(data=request.data, instance=instance)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({'result': serializer.data})
        
        
    def delete(self, request, *args, **kwargs):
        pk = kwargs.get('pk', None)
        if not pk:
            return Response({'result': 'Добавьте к URL id записи!'})
        
        try:
            instance = Survey.objects.get(pk=pk)
        except:
            return Response({'result': 'Объект с данным id не найден!'})
        
        Survey.objects.get(pk=pk).delete()
        return Response({'result': 'Объект удалён!'})
        
        
        
class QuestionListAndCreateAPIView(views.APIView):
    pass
class QuestionGetPatchDeleteAPIView(views.APIView):
    pass
class AnswerListAndCreateAPIView(views.APIView):
    pass
class AnswerGetPatchDeleteAPIView(views.APIView):
    pass



