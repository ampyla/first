# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2017-07-10 07:51
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0022_auto_20170710_1438'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='special',
            name='category',
        ),
        migrations.AddField(
            model_name='special',
            name='category',
            field=models.ManyToManyField(to='article.Category'),
        ),
    ]