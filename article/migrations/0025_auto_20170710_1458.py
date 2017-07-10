# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2017-07-10 07:58
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0024_auto_20170710_1455'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='special',
            name='category',
        ),
        migrations.AddField(
            model_name='special',
            name='category',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='article.Item'),
            preserve_default=False,
        ),
    ]