# Generated by Django 4.2.8 on 2024-02-03 08:53

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, verbose_name='Название')),
                ('author', models.CharField(max_length=100, verbose_name='Автор')),
                ('year_publication', models.PositiveSmallIntegerField(verbose_name='Год выпуска')),
                ('genre', models.CharField(choices=[('For children and parents', 'Детям и родителям'), ('Sports literature', 'Спортивная литература'), ('Business literature', 'Бизнес литература'), ('Scientific literature', 'Научная литература'), ('Children literature', 'Детская литература'), ('Biographies', 'Биографии'), ('Self-development', 'Саморазвитие'), ('History', 'История'), ('Health', 'Здоровье')], default='For children and parents', max_length=100, verbose_name='Жанр')),
                ('pages', models.PositiveSmallIntegerField(verbose_name='Страницы')),
                ('circulation', models.PositiveIntegerField(verbose_name='Тираж')),
                ('original_language', models.CharField(choices=[('chi', 'Китайский'), ('spa', 'Испанский'), ('eng', 'Английский'), ('hin', 'Хинди'), ('ara', 'Арабский'), ('rus', 'Русский'), ('jpn', 'Японский'), ('fra', 'Французский'), ('ger', 'Немецкий'), ('ita', 'Итальянский')], default='rus', max_length=50, verbose_name='Язык издания')),
                ('age_limit', models.CharField(choices=[('limit(0+)', '0+'), ('limit(6+)', '6+'), ('limit(12+)', '12+'), ('limit(16+)', '16+'), ('limit(18+)', '18+')], default='limit(0+)', max_length=30, verbose_name='Возрастное ограничение')),
            ],
            options={
                'verbose_name': 'Книга',
                'verbose_name_plural': 'Книги',
            },
        ),
    ]
