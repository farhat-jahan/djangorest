# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('expense_tracker', '0006_auto_20161119_1951'),
    ]

    operations = [
        migrations.AlterField(
            model_name='expensedetail',
            name='paid_date',
            field=models.DateTimeField(default=datetime.datetime(2016, 11, 19, 19, 52, 39, 528989, tzinfo=utc)),
        ),
    ]
