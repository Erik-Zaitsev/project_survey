# Generated by Django 4.2.8 on 2024-02-05 18:05

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='CustomUser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('username', models.CharField(max_length=50, unique=True, verbose_name='Пользователь')),
                ('email', models.CharField(max_length=150, unique=True, verbose_name='Почта')),
                ('date_joined', models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')),
                ('last_login', models.DateTimeField(auto_now=True, verbose_name='Последний вход')),
                ('is_staff', models.BooleanField(default=False, verbose_name='Администратор')),
                ('is_superuser', models.BooleanField(default=False, verbose_name='Суперпользователь')),
                ('is_active', models.BooleanField(default=True, verbose_name='В сети')),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.permission', verbose_name='user permissions')),
            ],
            options={
                'verbose_name': 'Пользователь',
                'verbose_name_plural': 'Пользователи',
            },
        ),
    ]
