# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Stock',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('modified_date', models.DateTimeField(auto_now=True)),
                ('ticker', models.CharField(max_length=10)),
                ('open', models.FloatField()),
                ('close', models.FloatField()),
                ('volume', models.IntegerField()),
            ],
            options={
                'db_table': 'stock',
            },
        ),
    ]
