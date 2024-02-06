from django.db import models
from user.models import CustomUser, CustomUserManager
from book.models import Book, Author

# Create your models here.
class Survey(models.Model):
    '''Класс для описания модели Опроса'''
    
    STATUS_SURVEY_CHOISES = (
        ('available', 'Доступен'),
        ('development', 'В разработке'),
        ('close', 'Закрыт'),
    )
    
    title = models.CharField(verbose_name='Название', max_length=150)
    date_creation = models.DateField(verbose_name='Дата создания', auto_now_add=True)
    creator = models.ForeignKey(CustomUser, verbose_name='Создатель', on_delete=models.CASCADE)
    status = models.CharField(verbose_name='Статус опроса', max_length=20,
                              choices=STATUS_SURVEY_CHOISES, default='close')
    repeat_passing = models.BooleanField(verbose_name='Повторное прохождение', default=False)
    book = models.ManyToManyField(Book, verbose_name='Книга', blank=True, default='Нет книги')
    author = models.ManyToManyField(Author, verbose_name='Автор', blank=True, default='Нет автора')
        
    class Meta:
        verbose_name = 'Опрос'
        verbose_name_plural = 'Опросы'
    
    def __str__(self):
        return self.title
    
    
    
class Question(models.Model):
    '''Класс для описания модели Вопроса'''
    
    QUESTION_TYPE_CHOICES = (
        ('Txt', 'Развёрнутый ответ'),
        ('OneChoice', 'Одиночный выбор'),
        ('ManyChoice', 'Множественный выбор'),
        ('DigitChoice', 'Число'),
        ('TimeChoice', 'Время'),
        ('DateChoice', 'Дата'),
        ('Scale', 'Шкала'),
    )
    
    survey = models.ForeignKey(Survey, verbose_name='Опрос', on_delete=models.CASCADE)
    question_name = models.CharField(verbose_name='Вопрос', max_length=255)
    question_type = models.CharField(verbose_name='Тип вопроса', max_length=40, 
                                     choices=QUESTION_TYPE_CHOICES, default='Txt')
    
    class Meta:
        verbose_name = 'Вопрос'
        verbose_name_plural = 'Вопросы'
    
    def __str__(self):
        return self.question_name
    
    
    
class Answer(models.Model):
    '''Класс для описания модели Ответа'''
    
    user = models.ForeignKey(CustomUser, verbose_name='Пользователь', on_delete=models.CASCADE)
    question = models.ForeignKey(Question, verbose_name='Вопрос', on_delete=models.CASCADE)
    answer_text = models.TextField(verbose_name='Ответ')
    
    class Meta:
        verbose_name = 'Ответ'
        verbose_name_plural = 'Ответы'
        
    def __str__(self):
        return self.answer_text