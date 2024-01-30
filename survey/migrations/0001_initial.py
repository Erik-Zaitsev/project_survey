# Generated by Django 4.2.8 on 2024-01-30 17:53

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Answer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('answer_text', models.TextField(verbose_name='Ответ')),
            ],
            options={
                'verbose_name': 'Ответ',
                'verbose_name_plural': 'Ответы',
            },
        ),
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question_name', models.CharField(max_length=255, verbose_name='Вопрос')),
                ('question_type', models.CharField(choices=[('Txt', 'Развёрнутый ответ'), ('OneChoice', 'Одиночный выбор'), ('ManyChoice', 'Множественный выбор'), ('DigitChoice', 'Число'), ('TimeChoice', 'Время'), ('DateChoice', 'Дата'), ('Scale', 'Шкала')], default='Txt', max_length=40, verbose_name='Тип вопроса')),
            ],
            options={
                'verbose_name': 'Вопрос',
                'verbose_name_plural': 'Вопросы',
            },
        ),
        migrations.CreateModel(
            name='Survey',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=150, verbose_name='Название')),
                ('date_creation', models.DateField(auto_now_add=True, verbose_name='Дата создания')),
                ('status', models.CharField(choices=[('available', 'Доступен'), ('development', 'В разработке'), ('close', 'Закрыт')], default='close', max_length=20, verbose_name='Статус опроса')),
                ('repeat_passing', models.BooleanField(default=False, verbose_name='Повторное прохождение')),
            ],
            options={
                'verbose_name': 'Опрос',
                'verbose_name_plural': 'Опросы',
            },
        ),
    ]
