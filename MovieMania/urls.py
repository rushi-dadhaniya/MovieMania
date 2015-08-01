from django.conf.urls import include, url
from rest_framework.routers import DefaultRouter
from movieapp import views

router = DefaultRouter()
router.register(r'movies', views.MovieViewSet)
router.register(r'users', views.UserViewSet)
router.register(r'genre', views.GenreViewSet)
urlpatterns = [
    url(r'^', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
]
