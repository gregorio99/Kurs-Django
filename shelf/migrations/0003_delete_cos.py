# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shelf', '0002_cos'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Cos',
        ),
    ]
