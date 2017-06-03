"""my_blog URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from django.views.generic import TemplateView, ListView

from article.models import Article

from article import views as article_views
from comments.views import create_comment
from article.views import about_view
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    # url(r'^$', ListView.as_view(model=Article, template_name='article/index.html')),
    url(r'^$', article_views.ArticleView.as_view()),
    url(r'^curr_date/$', article_views.current_datetime, name='get_article'),
    url(r'^article/', include('article.urls', namespace='article')),
    url(r'create_comment/(?P<id>\d+)/$', create_comment, name='create_comment'),
    url(r'^about_me/$', TemplateView.as_view(template_name='about.html'), name='about_me')
]
if settings.DEBUG:
    urlpatterns+=static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)