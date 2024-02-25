from django.shortcuts import render, redirect, get_object_or_404
from blog.models import Category, Post
from django.db.models import Q
import datetime

def index(request):
    template = 'blog/index.html'
    post_list = Post.objects.select_related(
        'location',
        'author',
        'category'
    ).filter(
        Q(is_published=True)
        & Q(category__is_published=True)
        & Q(pub_date__lt=datetime.datetime.now())
    ).order_by(
        '-pub_date'
    )[0:5]  # Не нравится что множество запросов делается к БД (и оформление с переносом строк)
    context = {'post_list': post_list}
    return render(request, template, context)


def post_detail(request, id):
    template = 'blog/detail.html'
    post = get_object_or_404(
        Post.objects.select_related(
            'location',
            'category'
        ).filter(
            Q(pub_date__lt=datetime.datetime.now())
            & Q(is_published=True)
            & Q(category__is_published=True)
        ),
        pk=id)  # Не нравится что множество запросов делается к БД (и оформление с переносом строк)
    context = {'post': post}
    return render(request, template, context)


def category_posts(request, category_slug):
    template = 'blog/category.html'
    category = get_object_or_404(
        Category.objects.values(
            'title',
            'description',
            'slug',
            'is_published'
        ).filter(
            is_published=True
        ),
        slug=category_slug
    )  # Стоит ли ограничивать получение полей из таблицы с целью экономии ожидания получения ответа или лучше пусть получает все поля без метода values?
    post_list = Post.objects.select_related(
        'location',
        'author',
        'category'
    ).filter(
        Q(is_published=True)
        & Q(category__is_published=True)
        & Q(category__slug=category_slug)
        & Q(pub_date__lt=datetime.datetime.now())
    ).order_by(
        '-pub_date'
    )  # Не нравится что множество запросов делается к БД (и оформление с переносом строк)
    context = {
        'category': category,
        'post_list': post_list,
    }
    return render(request, template, context)
