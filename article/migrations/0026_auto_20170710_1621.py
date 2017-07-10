# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2017-07-10 09:21
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('contenttypes', '0002_remove_content_type_name'),
        ('article', '0025_auto_20170710_1458'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='special',
            name='category',
        ),
        migrations.AddField(
            model_name='special',
            name='content_type',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='contenttypes.ContentType'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='special',
            name='object_id',
            field=models.PositiveIntegerField(default=''),
            preserve_default=False,
        ),
    ]