# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType

class Category(models.Model):
    name = models.CharField(max_length=255, verbose_name='Название категории')
    image = models.ImageField(upload_to='images//%Y/%m/%d')
    alt = models.CharField(max_length=245, verbose_name="Подсказка")
    alias = models.SlugField(verbose_name='Alias категории')

    class Meta:
        verbose_name =u"Категория"
        verbose_name_plural =u"Категории"
    def __unicode__(self):
        return u'Категория %s' % self.name


class Item(models.Model):
    name = models.CharField(max_length=255, verbose_name="Название товара")
    image = models.ImageField(upload_to='images//%Y/%m/%d')
    file = models.FileField(upload_to='images//%Y/%m/%d',blank=True,verbose_name="Скачать каталог")
    alias = models.SlugField(verbose_name="Alias товара")
    alt = models.CharField(max_length=255, verbose_name="Подсказка")
    caption_slider=models.CharField(max_length=255,verbose_name="Заголовок слайдера")
    text_in_slider=models.TextField(max_length=255,verbose_name="Текст на слайдере")
    content = RichTextUploadingField(blank=True,default='')

    category = models.ForeignKey(Category)

    class Meta:
        verbose_name ="Товар"
        verbose_name_plural ="Товары"

    def __unicode__(self):
        return 'Товар %s' % self.name

class SubItem(models.Model):

    name = models.CharField(max_length=255, verbose_name="Название подтовара")
    image = models.ImageField(upload_to='images//%Y/%m/%d')
    alias = models.SlugField(verbose_name="Alias товара")
    alt = models.CharField(max_length=255, verbose_name="Подсказка")
    caption_slider = models.CharField(max_length=255, verbose_name="Заголовок слайдера")
    text_in_slider = models.TextField(max_length=255, verbose_name="Текст на слайдере")
    content = RichTextUploadingField(blank=True, default='')
    category = models.ForeignKey(Item, blank=True, null=True)

    class Meta:
        verbose_name = "Под Товар"
        verbose_name_plural = "Под Товары"

    def __unicode__(self):
        return 'Под Товар %s' % self.name

class Special(models.Model):
    name = models.CharField(max_length=255, verbose_name="Название")
    price = models.IntegerField(max_length=50, verbose_name="Цена")
    category = models.ForeignKey(Category, blank=True, null=True)
    item = models.ForeignKey(Item, blank=True, null=True)
    alias = models.SlugField(verbose_name="Alias товара")

    class Meta:
        verbose_name = "Спецпредложение"
        verbose_name_plural = "Спецпредложения"

    def __unicode__(self):
        return 'Спецпредложение %s' % self.name


class About (models.Model):
    title = models.CharField(max_length=255, verbose_name="Заголовок")
    content = RichTextUploadingField(blank=True, default='')
    alias = models.SlugField(verbose_name="Alias о_компании")

    class Meta:
        verbose_name ="О компании"
        verbose_name_plural = "О компании"

    def __unicode__(self):
        return 'О компании %s' % self.title

class Slider(models.Model):
    image = models.ImageField(upload_to='images//%Y/%m/%d')
    url = models.URLField(blank=True, null=True)

    class Meta:
        verbose_name="Слайдер"
        verbose_name_plural= "Слайдер"
    def __unicode__(self):
        return 'Слайдер %s' % self.url