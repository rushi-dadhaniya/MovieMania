from rest_framework import serializers
from django.contrib.auth.models import User
from movieapp.models import Movie


class MovieSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')

    class Meta:
        model = Movie
        fields = ('url', 'name', 'director', 'popularity', 'movie_mania_score', 'duration', 'genre', 'owner')


class UserSerializers(serializers.ModelSerializer):
    movies = serializers.HyperlinkedRelatedField(many=True, queryset=Movie.objects.all(), view_name='movie-detail')

    class Meta:
        model = User
        fields = ('id', 'username', 'movies')
