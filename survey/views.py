from rest_framework import views, generics
from rest_framework.response import Response
from .models import Survey, Question, Answer
from .serializers import SurveySerializer, QuestionSerializer, AnswerSerializer
from django.forms import model_to_dict
from services import APIViewPagination


# Create your views here.
class SurveyListAPIView(generics.ListAPIView):
    queryset = Survey.objects.all()
    serializer_class = SurveySerializer
    pagination_class = APIViewPagination
    
    
class QuestionListAPIView(generics.ListAPIView):
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer
    pagination_class = APIViewPagination
    
    
class AnswerListAPIView(generics.ListAPIView):
    queryset = Answer.objects.all()
    serializer_class = AnswerSerializer
    pagination_class = APIViewPagination



class SurveyAPIView(views.APIView):
    pass
class QuestionAPIView(views.APIView):
    pass
class AnswerAPIView(views.APIView):
    pass
