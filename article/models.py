# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=255, verbose_name='Название товара')
    image = models.ImageField(upload_to='/media/images')
    url = models.URLField()
    alias = models.SlugField(verbose_name='Alias категории')
    class Meta:
        verbose_name ="Категория"
        verbose_name_plural ="Категории"
    def __str__(self):
        return 'Категория %s' % self.name