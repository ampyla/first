# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2017-06-24 16:00
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0010_category_alt'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='image',
            field=models.ImageField(upload_to='images//%Y/%m/%d'),
        ),
    ]