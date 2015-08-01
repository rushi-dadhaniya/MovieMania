# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Genre',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('genre', models.CharField(max_length=100, null=True)),
            ],
            options={
                'ordering': ('genre',),
            },
        ),
        migrations.CreateModel(
            name='Movie',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('movie_name', models.CharField(max_length=100)),
                ('director', models.CharField(max_length=100)),
                ('popularity', models.FloatField()),
                ('movie_mania_score', models.FloatField()),
                ('duration', models.CharField(max_length=20)),
                ('genre', models.ManyToManyField(to='movieapp.Genre')),
                ('owner', models.ForeignKey(related_name='movies', default=1, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ('movie_name',),
            },
        ),
    ]
