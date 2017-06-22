# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=255, verbose_name='Название категории')
    image = models.ImageField(upload_to='images//%Y/%m/%d')
    alias = models.SlugField(verbose_name='Alias категории')
    class Meta:
        verbose_name =u"Категория"
        verbose_name_plural =u"Категории"
    def __unicode__(self):
        return u'Категория %s' % self.name


class Item(models.Model):
    name = models.CharField(max_length=255, verbose_name="Название товара")
    image = models.ImageField(upload_to="/static/media/images")
    alias = models.SlugField(verbose_name="Alias товара")
    category = models.ForeignKey(Category)

    class Meta:
        verbose_name ="Товар"
        verbose_name_plural ="Товары"

    def __str__(self):
        return 'Товар %s' % self.name