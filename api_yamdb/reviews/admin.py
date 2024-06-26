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
    search_fields = ('author__username',)


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
    search_fields = ('author__username',)


@admin.register(Title)
class TitleAdmin(admin.ModelAdmin):
    list_display = (
        'pk',
        'name',
        'year',
        'description',
        'category',
        'get_genres'
    )
    list_filter = (
        'name',
        'year'
    )
    search_fields = (
        'name',
        'year'
    )
    list_editable = (
        'category',
    )

    @admin.display(description='Жанры')
    def get_genres(self, obj):
        genre_str = ''
        for genre in obj.genre.all():
            genre_str.join(genre.name)
        return genre_str


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
