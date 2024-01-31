from rest_framework import serializers
from .models import Survey, Question, Answer


class SurveySerializer(serializers.ModelSerializer):
    creator = serializers.SerializerMethodField()
    
    class Meta:
        model = Survey
        fields = [
            'id',
            'title',
            'date_creation',
            'creator',
            'status',
            'repeat_passing',
        ]
        
    @staticmethod
    def get_creator(obj):
        return obj.creator.username
    
    
    
class QuestionSerializer(serializers.ModelSerializer):
    survey = serializers.SerializerMethodField()
    
    class Meta:
        model = Question
        fields = [
            'survey',
            'question_name',
            'question_type',
        ]
        
    @staticmethod
    def get_survey(obj):
        return obj.survey.title
    
    
    
class AnswerSerializer(serializers.ModelSerializer):
    user = serializers.SerializerMethodField()
    question = serializers.SerializerMethodField()
    
    class Meta:
        model = Answer
        fields = [
            'user',
            'question',
            'answer_text',
        ]
        
    @staticmethod
    def get_user(obj):
        return obj.user.username
    
    @staticmethod
    def get_question(obj):
        return obj.question.question_name