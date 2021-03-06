#- * - coding: utf - 8 -*-
#import sys
#sys.setdefaultencoding("utf-8")

from django.contrib import admin
from models import *



class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)

class ItemAdmin(admin.ModelAdmin):
    list_display = ('id','name',)



class SubItemAdmin(admin.ModelAdmin):
    list_display = ('name',)



class SpecialAdmin(admin.ModelAdmin):
    list_display = ('name',)


class AboutAdmin(admin.ModelAdmin):
    list_display = ('title',)


class SliderAdmin(admin.ModelAdmin):
    list_display =('url',)

# Register your models here.
#class ArticleInline(admin.StackedInline):
#	model = Comments
#	extra = 2


#class ArticleAdmin(admin.ModelAdmin):
#	fields = ['article_title', 'article_text','article_date']
#	inlines = [ArticleInline]
#	list_filter = ['article_date']

admin.site.register(Category, CategoryAdmin)
admin.site.register(Item, ItemAdmin)
admin.site.register(SubItem, SubItemAdmin)
admin.site.register(Special, SpecialAdmin)
admin.site.register(About, AboutAdmin)
admin.site.register(Slider,SliderAdmin)