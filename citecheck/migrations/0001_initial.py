# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='journal_info',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('Rank', models.IntegerField()),
                ('Title', models.CharField(max_length=3000)),
                ('Type', models.CharField(max_length=3000)),
                ('ISSN', models.CharField(max_length=3000)),
                ('SJR', models.FloatField()),
                ('H_index', models.IntegerField()),
                ('Total_Docs_Last_Year', models.IntegerField()),
                ('Total_Docs_3years', models.IntegerField()),
                ('Total_Refs', models.IntegerField()),
                ('Total_Cites_3years', models.IntegerField()),
                ('Cites_per_Doc_2years', models.FloatField(max_length=3000)),
                ('Ref_per_Doc', models.FloatField(max_length=3000)),
                ('Country', models.CharField(max_length=3000)),
                ('added', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
