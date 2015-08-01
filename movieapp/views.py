from django.contrib.auth.models import User
from rest_framework import permissions
from rest_framework import viewsets
from movieapp.models import Movie
from movieapp.models import Genre
from movieapp.serializers import MovieSerializer
from movieapp.serializers import GenreSerializer
from movieapp.serializers import UserSerializers
from movieapp.permissions import IsOwnerOrReadOnly


class GenreViewSet(viewsets.ModelViewSet):
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly, )


class MovieViewSet(viewsets.ModelViewSet):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly,)

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class UserViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializers
