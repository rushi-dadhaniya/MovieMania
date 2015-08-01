from rest_framework import serializers
from django.contrib.auth.models import User
from movieapp.models import Movie
from movieapp.models import Genre


class GenreSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Genre
        fields = ('genre', )


class MovieSerializer(serializers.HyperlinkedModelSerializer):

    owner = serializers.ReadOnlyField(source='owner.username')

    class Meta:
        model = Movie
        field = ('genre', 'name')


class GenreAndMovieSerializer(serializers.ModelSerializer):
    movies = MovieSerializer(many=True, read_only=True, source='movie_set')

    class Meta:
        model = Genre


class UserSerializers(serializers.ModelSerializer):
    movies = serializers.HyperlinkedRelatedField(many=True, queryset=Movie.objects.all(), view_name='movie-detail')

    class Meta:
        model = User
        fields = ('id', 'username', 'movies')
