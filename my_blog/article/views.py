# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, get_object_or_404
from article.models import Article
from django.http import JsonResponse
from comments.forms import CommentsForm

from django.views.generic import ListView

# Create your views here.
# def index(request):
#     return render(request, 'article/index.html', {'articles': Article.objects.all()})

class ArticleView(ListView):
    model = Article
    template_name = 'article/index.html'

    def get_context_data(self, **kwargs):
        context = super(ArticleView, self).get_context_data(**kwargs)
        context['my_text']='dkflkdlfkl'
        return context

def get_article(request, id, text='1212'):
    article=get_object_or_404(Article, id=id)
    if request.method == 'POST':
        form = CommentsForm(request.POST)
        if form.is_valid():
            c=form.save(commit=False)
            c.article=article
            c.author = request.user
            c.save()
    else:
        form = CommentsForm()
    data = {
        'article': article,
        'text': text,
        'form': form
    }
    return render(request, 'article/article.html', data)

from django.http import HttpResponse
import datetime

def current_datetime(request):
    now = datetime.datetime.now()
    html = "<html><body>It is now %s.<br/>%s<br/>%s</body></html>" % (now, request.path, str(request.GET['text']))
    return HttpResponse(html)

def about_view(request):
    return render(request, 'about.html')