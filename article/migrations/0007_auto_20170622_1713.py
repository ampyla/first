# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2017-06-22 10:13
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0006_auto_20170622_1711'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='image',
            field=models.ImageField(upload_to='images//%Y/%m/%d'),
        ),
    ]