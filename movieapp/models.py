from django.db import models


class Genre(models.Model):
    genre = models.CharField(max_length=100, default='')

    def __unicode__(self):
        return self.genre

    class Meta:
        ordering = ('genre',)


class Movie(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    movie_name = models.CharField(max_length=100, blank=False)
    director = models.CharField(max_length=100)
    popularity = models.FloatField()
    movie_mania_score = models.FloatField()
    duration = models.CharField(max_length=20)
    genre = models.ManyToManyField('Genre', default='')
    owner = models.ForeignKey('auth.User', related_name='movies', default=1)

    def __unicode__(self):
        return self.name

    class Meta:
        ordering = ('movie_name',)
