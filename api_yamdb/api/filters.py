from django_filters import filters, rest_framework

from reviews.models import Title


class TitleFilter(rest_framework.FilterSet):
    name = filters.CharFilter(field_name='name')
    genre = filters.CharFilter(field_name='genre__slug')
    category = filters.CharFilter(field_name='category__slug')

    class Meta:
        model = Title
        fields = (
            'name',
            'genre',
            'category',
            'year'
        )
