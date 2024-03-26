from django.contrib import admin

from reviews.models import Category, Comment, Genre, Review, Title


@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = (
        'pk',
        'score',
        'text',
        'author',
        'pub_date',
        'title'
    )
    list_filter = (
        'author',
        'score',
        'pub_date'
    )
    search_fields = ('author',)


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = (
        'pk',
        'author',
        'text',
        'review',
        'pub_date'
    )
    list_filter = (
        'author',
        'pub_date'
    )
    search_fields = ('author',)


@admin.register(Title)
class TitleAdmin(admin.ModelAdmin):
    list_display = (
        'pk',
        'name',
        'year',
        'description',
        'category'
    )
    list_filter = (
        'name',
        'year'
    )
    search_fields = (
        'name',
        'year'
    )


@admin.register(Genre)
class GenreAdmin(admin.ModelAdmin):
    list_display = (
        'pk',
        'name',
        'slug'
    )
    list_filter = ('name',)
    search_fields = ('name',)


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = (
        'pk',
        'name',
        'slug'
    )
    list_filter = ('name',)
    search_fields = ('name',)
