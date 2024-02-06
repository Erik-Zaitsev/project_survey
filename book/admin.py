from django.contrib import admin
from .models import Book, Author


# Register your models here.
@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ['name',]
    
    search_fields = ['name',]
    
    search_help_text = 'Поиск по полю: Имя и фамилия'


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = [
        'title',
        # 'author',
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
    
    search_help_text = 'Поиск книги по полям: Название, Автор, Год выпуска'
    
    fieldsets = (
        ('Основная информация',
        {'fields': ('title', 'author','year_publication', 'short_description',)}),
        ('Дополнительная информация',
        {'fields': ('genre', 'pages', 'circulation', 'original_language', 'age_limit', 'image_cover',)}),        
    )
    
    add_fieldsets = (
        ('Основная информация',
        {'fields': ('title', 'author','year_publication', 'short_description',)}),
        ('Дополнительная информация',
        {'fields': ('genre', 'pages', 'circulation', 'original_language', 'age_limit', 'image_cover',)}),        
    )
    
    

    
    