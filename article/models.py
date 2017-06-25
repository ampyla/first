# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=255, verbose_name='Название категории')
    image = models.ImageField(upload_to='images//%Y/%m/%d')
    alt = models.CharField(max_length=245, verbose_name="Подсказка")
    alias = models.SlugField(verbose_name='Alias категории')
    def get_products(self):
        Item.objects.filter(category=self)

    class Meta:
        verbose_name =u"Категория"
        verbose_name_plural =u"Категории"
    def __unicode__(self):
        return u'Категория %s' % self.name


class Item(models.Model):
    name = models.CharField(max_length=255, verbose_name="Название товара")
    image = models.ImageField(upload_to='images//%Y/%m/%d')
    alias = models.SlugField(verbose_name="Alias товара")
    alt = models.CharField(max_length=245, verbose_name="Подсказка")
    category = models.ForeignKey(Category)

    class Meta:
        verbose_name ="Товар"
        verbose_name_plural ="Товары"

    def __unicode__(self):
        return 'Товар %s' % self.name