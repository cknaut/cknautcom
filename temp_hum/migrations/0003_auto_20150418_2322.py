# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('temp_hum', '0002_auto_20150418_2033'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='data_point',
            options={'get_latest_by': 'created'},
        ),
    ]
