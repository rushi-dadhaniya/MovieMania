from django.db import models


class Movie(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    name = models.CharField(max_length=100, blank=False)
    director = models.CharField(max_length=100)
    popularity = models.FloatField()
    movie_mania_score = models.FloatField()
    duration = models.CharField(max_length=20)
    genre = models.CharField(max_length=200)
