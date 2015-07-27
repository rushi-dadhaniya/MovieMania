# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('movieapp', '0003_auto_20150726_1630'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movie',
            name='owner',
            field=models.ForeignKey(related_name='movies', to=settings.AUTH_USER_MODEL),
        ),
    ]
