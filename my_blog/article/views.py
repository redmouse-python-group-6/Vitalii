# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from article.models import Article

# Create your views here.
def index(request):
    return render(request, 'index.html',{'articles': Article.objects.all()} )