# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('expense_tracker', '0009_auto_20161119_2034'),
    ]

    operations = [
        migrations.AlterField(
            model_name='expensedetail',
            name='modified_date',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='expensedetail',
            name='paid_date',
            field=models.DateTimeField(default=datetime.datetime(2016, 11, 19, 20, 49, 45, 559141, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='userdetail',
            name='modified_date',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
