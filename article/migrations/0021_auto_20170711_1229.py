# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2017-07-11 05:29
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0020_special'),
    ]

    operations = [
        migrations.AddField(
            model_name='special',
            name='category',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='article.Category'),
        ),
        migrations.AddField(
            model_name='special',
            name='item',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='article.Item'),
        ),
    ]
