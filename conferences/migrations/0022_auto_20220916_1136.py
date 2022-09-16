# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2022-09-16 03:36
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('conferences', '0021_auto_20170605_1219'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='active',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='conference',
            name='abstract_deadline',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2022, 10, 1, 3, 36, 20, 595863, tzinfo=utc), verbose_name='Deadline of Abstract Submission'),
        ),
        migrations.AlterField(
            model_name='conference',
            name='end_date',
            field=models.DateField(default=datetime.datetime(2022, 10, 18, 3, 36, 20, 595863, tzinfo=utc), verbose_name='Date Ended'),
        ),
        migrations.AlterField(
            model_name='conference',
            name='paper_deadline',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2022, 10, 6, 3, 36, 20, 595863, tzinfo=utc), verbose_name='Deadline of Paper Submission'),
        ),
        migrations.AlterField(
            model_name='conference',
            name='start_date',
            field=models.DateField(default=datetime.datetime(2022, 10, 16, 3, 36, 20, 595863, tzinfo=utc), verbose_name='Date Started'),
        ),
    ]
