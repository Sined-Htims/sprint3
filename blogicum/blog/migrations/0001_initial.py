# Generated by Django 3.2.16 on 2024-02-22 07:57

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_created=True, blank=True, verbose_name='Время создания')),
                ('is_published', models.BooleanField(blank=True, default=True, verbose_name='Опубликовано')),
                ('title', models.CharField(blank=True, max_length=256, verbose_name='Категория')),
                ('slug', models.SlugField(blank=True, unique=True)),
                ('description', models.TextField(blank=True, verbose_name='Описание категории')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Location',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_created=True, blank=True, verbose_name='Время создания')),
                ('is_published', models.BooleanField(blank=True, default=True, verbose_name='Опубликовано')),
                ('name', models.CharField(blank=True, max_length=256, verbose_name='Локация')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_created=True, blank=True, verbose_name='Время создания')),
                ('is_published', models.BooleanField(blank=True, default=True, verbose_name='Опубликовано')),
                ('title', models.CharField(blank=True, max_length=256, verbose_name='Загаловок поста')),
                ('text', models.TextField(blank=True, verbose_name='Содержание поста')),
                ('pub_date', models.DateTimeField(blank=True, verbose_name='Время публикации')),
                ('author', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, related_name='Pub', to=settings.AUTH_USER_MODEL)),
                ('category', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='Categories', to='blog.category')),
                ('location', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='Maps', to='blog.location')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
