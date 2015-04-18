# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('temp_hum', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='reading',
            new_name='data_point',
        ),
    ]
