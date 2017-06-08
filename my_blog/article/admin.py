# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from article.models import Article, Category
# Register your models here.
class ArticleAdmin(admin.ModelAdmin):
    list_display = ('title', 'body')
    search_fields = ('title', 'body')
    view_on_site = True
    # radio_fields = {'category': admin.HORIZONTAL}
    raw_id_fields = ('category',)
    save_as = False
admin.site.register(Article, ArticleAdmin)

class ArticleInline(admin.StackedInline):
    model = Article

class CategoryAdmin(admin.ModelAdmin):
     inlines = [
         ArticleInline
     ]
admin.site.register(Category, CategoryAdmin)