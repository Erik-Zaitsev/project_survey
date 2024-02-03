from django.contrib import admin
from .models import Book


# Register your models here.
@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = [
        'title',
        'author',
        'year_publication',
        'genre',
        'pages',
        'circulation',
        'original_language',
        'age_limit',
    ]
    
    list_filter = [
        'genre',
        'original_language',
        'age_limit',
    ]
    
    search_fields = [
        'title',
        'author',
        'year_publication',
    ]
    
    search_help_text = 'Поиск книги по полям: название, автор, год выпуска'
    
    fieldsets = (
        ('Основная информация',
        {'fields': ('title', 'author','year_publication',)}),
        ('Дополнительная информация',
        {'fields': ('genre', 'pages', 'circulation', 'original_language', 'age_limit',)}),        
    )
    
    add_fieldsets = (
        ('Основная информация',
        {'fields': ('title', 'author','year_publication',)}),
        ('Дополнительная информация',
        {'fields': ('genre', 'pages', 'circulation', 'original_language', 'age_limit',)}),        
    )