from django.db import models
from django.contrib.auth import get_user_model


User = get_user_model()  # какие поля там зашиты?


class PublishedCreated(models.Model):  # может нужно в другом месте ее использовать? Например core?
    """Абстрактная модель. Поля: Published, Created"""

    is_published = models.BooleanField(
        default=True,
        blank=True,
        verbose_name='Опубликовано',
        help_text='Снимите галочку, чтобы скрыть публикацию.'
    )
    created_at = models.DateTimeField(
        auto_now_add=True,
        blank=True,
        verbose_name='Добавлено'
    )

    class Meta:
        abstract = True


class Category(PublishedCreated):
    """Модель категорий(тематическая категория)"""

    title = models.CharField(
        max_length=256,
        blank=True,
        verbose_name='Заголовок'
    )
    slug = models.SlugField(
        blank=True,
        unique=True,
        verbose_name='Идентификатор',
        help_text='Идентификатор страницы для URL; разрешены символы латиницы, цифры, дефис и подчёркивание.'
    )
    description = models.TextField(
        blank=True,
        verbose_name='Описание'
    )

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'категория'
        verbose_name_plural = 'Категории'


class Location(PublishedCreated):
    """Модель локации(географическая метка)"""

    name = models.CharField(
        max_length=256,
        blank=True,
        verbose_name='Название места'
    )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'местоположение'
        verbose_name_plural = 'Местоположения'


class Post(PublishedCreated):
    """Модель публикации"""

    title = models.CharField(
        max_length=256,
        blank=True,
        verbose_name='Загаловок'
    )
    text = models.TextField(blank=True, verbose_name='Текст')
    pub_date = models.DateTimeField(
        blank=True,
        verbose_name='Дата и время публикации',
        help_text='Если установить дату и время в будущем — можно делать отложенные публикации.'
    )  # 2 даты по заданию, зачем?
    author = models.ForeignKey(
        User,
        blank=True,
        related_name='Pub',
        on_delete=models.CASCADE,
        verbose_name='Автор публикации'
    )  # как задавать имя в related_name?
    location = models.ForeignKey(
        'Location',
        null=True,
        blank=False,
        related_name='Maps',
        on_delete=models.SET_NULL,
        verbose_name='Местоположение'
    )
    category = models.ForeignKey(
        'Category',
        null=True,
        blank=False,
        related_name='Categories',
        on_delete=models.SET_NULL,
        verbose_name='Категория'
    )

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'публикация'
        verbose_name_plural = 'Публикации'
