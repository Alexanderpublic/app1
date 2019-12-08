#-*- coding: utf-8 -*-

from __future__ import unicode_literals
from django.db import models


class Article(models.Model):
    class Meta():
        db_table = 'article'
    article_title = models.CharField(max_length=200)
    article_text = models.TextField()
    pub_date = models.DateTimeField(auto_now_add=True)


class Comment (models.Model):
    class Meta():
        db_table = 'comment'
    comment_text = models.TextField(verbose_name="Текст комментария")
    pub_date = models.DateTimeField(auto_now_add=True)
    comment_article = models.ForeignKey(Article)
    creator = models.TextField()