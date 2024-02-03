from rest_framework import serializers
from .models import Survey, Question, Answer


class SurveyListAndGetSerializer(serializers.ModelSerializer):
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
    

class SurveyPostAndPatchSerializer(serializers.ModelSerializer):    
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
    
    def save(self, **kwargs):
        kwargs.update({
            'title': self.validated_data['title'],
            'date_creation': self.validated_data['date_creation'],
            'creator': self.validated_data['creator'],
            'status': self.validated_data['status'],
            'repeat_passing': self.validated_data['repeat_passing'],
        })
        
        instance = super().save(**kwargs)
        return instance
    
    def create(self, validated_data):
        return Survey.objects.create(**validated_data)
    
    def update(self, instance, validated_data):
        instance.title = validated_data.get('title', instance.title)
        instance.date_creation = validated_data.get('date_creation', instance.date_creation)
        instance.creator = validated_data.get('creator', instance.creator)
        instance.status = validated_data.get('status', instance.status)
        instance.repeat_passing = validated_data.get('repeat_passing', instance.repeat_passing)
        instance.save()
        return instance
    

    
    
    
class QuestionListAndGetSerializer(serializers.ModelSerializer):
    survey = serializers.SerializerMethodField()
    
    class Meta:
        model = Question
        fields = [
            'id',
            'survey',
            'question_name',
            'question_type',
        ]
        
    @staticmethod
    def get_survey(obj):
        return obj.survey.title
    
    
class QuestionPostAndPatchSerializer(serializers.ModelSerializer):
    class Meta:
        model = Question
        fields = [
            'id',
            'survey',
            'question_name',
            'question_type',
        ]
        
    def create(self, validated_data):
        return Question.objects.create(**validated_data)
    
    def update(self, instance, validated_data):
        pass
    
    
    
class AnswerListAndGetSerializer(serializers.ModelSerializer):
    user = serializers.SerializerMethodField()
    question = serializers.SerializerMethodField()
    
    class Meta:
        model = Answer
        fields = [
            'id',
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
    
    
class AnswerPostAndPatchSerializer(serializers.ModelSerializer):
    class Meta:
        model = Answer
        fields = [
            'id',
            'user',
            'question',
            'answer_text',
        ]

    def create(self, validated_data):
        return Answer.objects.create(**validated_data)
    
    def update(self, instance, validated_data):
        pass
        