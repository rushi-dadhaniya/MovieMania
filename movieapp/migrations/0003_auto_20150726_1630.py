# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('movieapp', '0002_movie_owner'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movie',
            name='owner',
            field=models.ForeignKey(related_name='movieapp', to=settings.AUTH_USER_MODEL),
        ),
    ]
