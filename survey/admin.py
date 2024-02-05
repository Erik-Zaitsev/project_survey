from django.contrib import admin
from .models import Survey, Question, Answer

# Register your models here.
@admin.register(Survey)
class SurveyAdmin(admin.ModelAdmin):
    list_display = [
        'title',
        'date_creation',
        'creator',
        'status',
        'repeat_passing',
        'book',
    ]
    
    list_filter = ['status', 'repeat_passing',]
    
    readonly_fields = ['date_creation',]
    
    search_fields = ['title',]
    
    search_help_text = 'Поиск по названию опроса'
    
    
    
@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):
    list_display = [
        'survey',
        'question_name',
        'question_type',
    ]
    
    list_filter = ['question_type',]
    
    search_fields = ['question_name',]
    
    search_help_text = 'Поиск по названию вопроса'
    
    
    
@admin.register(Answer)
class AnswerAdmin(admin.ModelAdmin):
    list_display = [
        'user',
        'question',
        'answer_text',
    ]
    
    