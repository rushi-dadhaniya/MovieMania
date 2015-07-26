from rest_framework import serializers
from django.contrib.auth.models import User
from movieapp.models import Movie


class MovieSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')

    class Meta:
        model = Movie
        fields = ('id', 'name', 'director', 'popularity', 'movie_mania_score', 'duration', 'genre', 'owner')


class UserSerializers(serializers.ModelSerializer):
    movies = serializers.PrimaryKeyRelatedField(many=True, queryset=Movie.objects.all())

    class Meta:
        model = User
        fields = ('id', 'username', 'movies')
