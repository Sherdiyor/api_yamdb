from django.urls import include, path
from rest_framework.routers import DefaultRouter

from .views import (UserViewSet,
                    get_jwt_token,
                    send_confirmation_code,
                    ReviewViewSet,
                    GenreViewSet,
                    CategoryViewSet,
                    CommentViewSet,
                    TitleViewSet,
                    )

v1_router = DefaultRouter()
v1_router.register('users', UserViewSet)
v1_router.register(r'titles/(?P<title_id>\d+)/reviews',
                   ReviewViewSet, basename='review')
v1_router.register(r'titles/(?P<title_id>\d+)/reviews/'
                   r'(?P<review_id>\d+)/comments',
                   CommentViewSet, basename='comment')
v1_router.register('categories', CategoryViewSet)
v1_router.register('genres', GenreViewSet)
v1_router.register('titles', TitleViewSet)


v1_auth_patterns = [
    path('signup/', send_confirmation_code, name='send_confirmation_code'),
    path('token/', get_jwt_token, name='get_token'),
]

urlpatterns = [
    path('v1/auth/', include(v1_auth_patterns)),
    path('v1/', include(v1_router.urls)),
]
