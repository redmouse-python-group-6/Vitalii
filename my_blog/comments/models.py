# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from article.models import Article
from django.contrib.auth.models import User

# Create your models here.
class Comments(models.Model):
    article=models.ForeignKey(Article)
    title=models.CharField(max_length=10)
    body = models.TextField()
    date_create = models.DateTimeField(auto_now_add=True)
    author=models.ForeignKey(User)
    is_publick=models.BooleanField(default=False)

