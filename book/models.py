from django.db import models


# Create your models here.
class Author(models.Model):
    '''Класс для модели автора'''
    name = models.CharField(verbose_name='Имя и фамилия', max_length=150)
    
    class Meta:
        verbose_name = 'Автор'
        verbose_name_plural = 'Авторы'
        
    def __str__(self):
        return self.name


class Book(models.Model):
    '''Класс для модели книги'''
    BOOK_GENRE_CHOICES = (
        ('For children and parents', 'Детям и родителям'),
        ('Sports literature', 'Спортивная литература'),
        ('Business literature', 'Бизнес литература'),
        ('Scientific literature', 'Научная литература'),
        ('Children literature', 'Детская литература'),
        ('Biographies', 'Биографии'),
        ('Self-development', 'Саморазвитие'),
        ('History', 'История'),
        ('Health', 'Здоровье'),
        ('Finance', 'Финансы'),
    )
    
    BOOK_LANGUAGE_CHOICES = (
        ('chi', 'Китайский'),
        ('spa', 'Испанский'),
        ('eng', 'Английский'),
        ('hin', 'Хинди'),
        ('ara', 'Арабский'),
        ('rus', 'Русский'),
        ('jpn', 'Японский'),
        ('fra', 'Французский'),
        ('ger', 'Немецкий'),
        ('ita', 'Итальянский'),
    )
    
    BOOK_AGE_LIMIT_CHOICES = (
        ('limit(0+)', '0+'),
        ('limit(6+)', '6+'),
        ('limit(12+)', '12+'),
        ('limit(16+)', '16+'),
        ('limit(18+)', '18+'),
    )
    
    title = models.CharField(verbose_name='Название', max_length=255)
    author = models.ManyToManyField(Author, verbose_name='Автор')
    year_publication = models.PositiveSmallIntegerField(verbose_name='Год выпуска')
    genre = models.CharField(verbose_name='Жанр', choices=BOOK_GENRE_CHOICES, 
                             max_length=100, default='For children and parents')
    short_description = models.TextField(verbose_name='Краткое описание', null=True)
    pages = models.PositiveSmallIntegerField(verbose_name='Страницы')
    circulation = models.PositiveIntegerField(verbose_name='Тираж')
    original_language = models.CharField(verbose_name='Язык издания', choices=BOOK_LANGUAGE_CHOICES, 
                             max_length=50, default='rus')
    age_limit = models.CharField(verbose_name='Возрастное ограничение', choices=BOOK_AGE_LIMIT_CHOICES, 
                             max_length=30, default='limit(0+)')
    # image_cover = models.ImageField(verbose_name='Обложка', upload_to='book/static/book/images/',
    #                          default='no_cover.jpeg')
    
    class Meta:
        verbose_name = 'Книга'
        verbose_name_plural = 'Книги'
        
    def __str__(self):
        return self.title
    
    
    
