from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator


class Genre(models.Model):
    genre = models.CharField(max_length=100, null=True, unique=True)

    def __unicode__(self):
        return self.genre

    class Meta:
        ordering = ('genre',)


class Movie(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    movie_name = models.CharField(max_length=100, blank=False)
    director = models.CharField(max_length=100)
    popularity = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(100)])
    movie_mania_score = models.DecimalField(max_digits=3, decimal_places=1, validators=[MinValueValidator(0), MaxValueValidator(10)])
    duration = models.CharField(max_length=20)
    genre = models.ManyToManyField('Genre')
    owner = models.ForeignKey('auth.User', related_name='movies', default=1)

    def __unicode__(self):
        return self.name

    class Meta:
        ordering = ('movie_name',)
