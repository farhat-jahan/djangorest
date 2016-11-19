# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('expense_tracker', '0005_auto_20161020_2127'),
    ]

    operations = [
        migrations.AlterField(
            model_name='expensedetail',
            name='paid_date',
            field=models.DateTimeField(default=datetime.datetime(2016, 11, 19, 19, 51, 39, 904316, tzinfo=utc)),
        ),
    ]
