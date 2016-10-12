# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.conf import settings
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('expense_tracker', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='expensedetail',
            name='balance',
            field=models.DecimalField(null=True, max_digits=19, decimal_places=2),
        ),
        migrations.AlterField(
            model_name='expensedetail',
            name='description',
            field=models.TextField(null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='expensedetail',
            name='paid_date',
            field=models.DateTimeField(default=datetime.datetime(2016, 10, 12, 21, 44, 55, 864534, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='expensedetail',
            name='payment_mode',
            field=models.CharField(blank=True, max_length=10, null=True, choices=[(b'Cash', b'Cash'), (b'Wallet', b'Wallet'), (b'Card', b'Card'), (b'Check', b'Check'), (b'NetBanking', b'NetBanking'), (b'Others', b'Others')]),
        ),
        migrations.AlterField(
            model_name='expensedetail',
            name='user_detail',
            field=models.ForeignKey(to=settings.AUTH_USER_MODEL),
        ),
    ]
