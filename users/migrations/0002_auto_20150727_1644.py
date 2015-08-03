# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bibliouser',
            name='avatar',
            field=models.ImageField(null=True, upload_to='avatars/', blank=True),
        ),
        migrations.AlterField(
            model_name='bibliouser',
            name='phone',
            field=models.CharField(blank=True, max_length=15),
        ),
    ]
