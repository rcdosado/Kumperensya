# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-05-09 02:36
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('conferences', '0018_auto_20170509_1025'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='category',
            options={'ordering': ('name',), 'verbose_name_plural': 'Categories'},
        ),
        migrations.AddField(
            model_name='conference',
            name='categories',
            field=models.ManyToManyField(null=True, to='conferences.Category', verbose_name='Categories Belong to'),
        ),
        migrations.AlterField(
            model_name='conference',
            name='abstract_deadline',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2017, 5, 24, 2, 36, 15, 259604, tzinfo=utc), verbose_name='Deadline of Abstract Submission'),
        ),
        migrations.AlterField(
            model_name='conference',
            name='end_date',
            field=models.DateField(default=datetime.datetime(2017, 6, 10, 2, 36, 15, 259604, tzinfo=utc), verbose_name='Date Ended'),
        ),
        migrations.AlterField(
            model_name='conference',
            name='paper_deadline',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2017, 5, 29, 2, 36, 15, 259604, tzinfo=utc), verbose_name='Deadline of Paper Submission'),
        ),
        migrations.AlterField(
            model_name='conference',
            name='start_date',
            field=models.DateField(default=datetime.datetime(2017, 6, 8, 2, 36, 15, 259604, tzinfo=utc), verbose_name='Date Started'),
        ),
    ]