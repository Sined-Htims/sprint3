from django.contrib import admin
from .models import Category, Location, Post


class PostInline(admin.StackedInline):
    model = Post
    extra = 1


class CategoryAdmin(admin.ModelAdmin):
    """Модель категории для изменения в админ-зоне"""

    inlines = (
        PostInline,
    )
    list_display = (
        'title',
        'is_published',
        'slug',
        'created_at',
    )
    list_editable = ('is_published',)
    search_fields = ('title',)


class PostAdmin(admin.ModelAdmin):
    """Модель публикации для изменения в админ-зоне"""

    list_display = (
        'title',
        'is_published',
        'category',
        'author',
        'location',
        'created_at',
        'pub_date',
    )
    list_editable = (
        'is_published',
        'category',
    )
    list_filter = ('category',)
    search_fields = ('title',)


admin.site.register(Category, CategoryAdmin)
admin.site.register(Location)
admin.site.register(Post, PostAdmin)
