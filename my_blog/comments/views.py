# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect

from comments.forms import CommentsForm
from comments.models import Comments
from article.models import Article
from django.urls import reverse

# Create your views here.
def create_comment(request, id):
    article = Article.objects.get(id=id)
    if request.method == 'POST':
        form = CommentsForm(request.POST)
        if form.is_valid():
            c=form.save(commit=False)
            c.article=article
            c.author = request.user
            c.save()
    # c = Comments(
    #     title=request.POST.get('title', 'Title'),
    #     body=request.POST.get('body', 'No text'),
    #     article=article
    # )
    # c.save()
    # return redirect('/article/%s/'%article.id)
    return redirect(reverse('article:get_article', kwargs={'id':article.id}))