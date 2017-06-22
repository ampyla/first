
from django.contrib import admin
from models import *



class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)

class ItemAdmin(admin.ModelAdmin):
    list_display = ('id','name',)




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

