# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('expense_tracker', '0002_auto_20161012_2144'),
    ]

    operations = [
        migrations.AlterField(
            model_name='expensedetail',
            name='paid_date',
            field=models.DateTimeField(default=datetime.datetime(2016, 10, 12, 21, 45, 17, 762815, tzinfo=utc)),
        ),
    ]
