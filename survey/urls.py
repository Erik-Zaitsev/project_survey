from django.urls import path, include
from survey.views import (SurveyListAPIView, QuestionListAPIView, AnswerListAPIView, 
                          SurveyAPIView, QuestionAPIView, AnswerAPIView)


urlpatterns = [
    path('', SurveyListAPIView().as_view()),
    path('<int:pk>/', SurveyAPIView().as_view()),
    path('questions/', QuestionListAPIView().as_view()),
    path('questions/<int:pk>/', QuestionAPIView().as_view()),
    path('answers/', AnswerListAPIView().as_view()),
    path('answers/<int:pk>/', AnswerAPIView().as_view()),

]