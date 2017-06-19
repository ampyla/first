from __future__ import unicode_literals

from django.db import models

class Article(models.Model):
	class Meta:
		db_table = "article"
	article_title = models.CharField(max_length = 200)
	article_text = models.TextField()
	article_date = models.DateTimeField()
	article_like = models.IntegerField(default = 0)

# Create your models here.
class Comments(models.Model):
 	class Meta():
 		db_table = 'comments'
 	comments_text = models.TextField()
 	comments_article = models.ForeignKey(Article)
