# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='ExpenseDetail',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('modified_date', models.DateTimeField(auto_now=True)),
                ('amount_spend', models.DecimalField(max_digits=19, decimal_places=2)),
                ('paid_for', models.CharField(max_length=15, choices=[(b'Trip and Travel', b'Trip and Travel'), (b'Grocery', b'Grocery'), (b'Parlour', b'Parlour'), (b'Cook', b'Cook'), (b'Maid', b'Maid'), (b'Food and Drinks', b'Food and Drinks'), (b'Gas', b'Gas'), (b'Others', b'Others')])),
                ('paid_date', models.DateTimeField(default=datetime.datetime(2016, 10, 12, 20, 55, 52, 144850, tzinfo=utc))),
                ('description', models.TextField()),
                ('payment_mode', models.CharField(max_length=10, choices=[(b'Cash', b'Cash'), (b'Wallet', b'Wallet'), (b'Card', b'Card'), (b'Check', b'Check'), (b'NetBanking', b'NetBanking'), (b'Others', b'Others')])),
                ('balance', models.DecimalField(max_digits=19, decimal_places=2)),
                ('user_detail', models.OneToOneField(to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'expencedetail',
            },
        ),
        migrations.CreateModel(
            name='UserDetail',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('modified_date', models.DateTimeField(auto_now=True)),
                ('address', models.CharField(max_length=30, blank=True)),
                ('user', models.OneToOneField(to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'userdetail',
            },
        ),
    ]
