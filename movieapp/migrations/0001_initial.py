# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Movie',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('name', models.CharField(max_length=100)),
                ('director', models.CharField(max_length=100)),
                ('popularity', models.FloatField()),
                ('movie_mania_score', models.FloatField()),
                ('duration', models.CharField(max_length=20)),
                ('genre', models.CharField(max_length=200)),
            ],
        ),
    ]
