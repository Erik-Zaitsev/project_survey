from django.urls import path, include
from survey.views import (SurveyListAndCreateAPIView, SurveyGetPatchDeleteAPIView,
                          QuestionListAndCreateAPIView, QuestionGetPatchDeleteAPIView,
                          AnswerListAndCreateAPIView, AnswerGetPatchDeleteAPIView)


urlpatterns = [
    path('', SurveyListAndCreateAPIView().as_view()),
    path('<int:pk>/', SurveyGetPatchDeleteAPIView().as_view()),
    path('questions/', QuestionListAndCreateAPIView().as_view()),
    path('questions/<int:pk>/', QuestionGetPatchDeleteAPIView().as_view()),
    path('answers/', AnswerListAndCreateAPIView().as_view()),
    path('answers/<int:pk>/', AnswerGetPatchDeleteAPIView().as_view()),
]