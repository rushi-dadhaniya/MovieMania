from movieapp.models import Movie
from rest_framework import serializers
from django.forms import widgets


class MovieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = ('id', 'name', 'director', 'popularity', 'movie_mania_score', 'duration', 'genre')

