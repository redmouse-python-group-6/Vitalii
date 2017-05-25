# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User

class Category(models.Model):
    title=models.CharField(max_length=10)
    description = models.TextField()
    slug = models.SlugField(unique=True)
    parent = models.ForeignKey('self', blank=True, null=True, default=None)

    def __str__(self):
        return self.title

    def get_all_article(self):
        return Article.objects.filter(category=self)

# Create your models here.
class Article(models.Model):
    title=models.CharField(max_length=100)
    body = models.TextField()
    date_create = models.DateTimeField(auto_now_add=True)
    date_update = models.DateTimeField(auto_now=True)
    author= models.ForeignKey(User)
    category = models.ForeignKey(Category, blank=True, null=True, default=None)


    def get_data_create_and_update(self):
        return "Create: %s Update: %s"%(self.date_create, self.date_update)




