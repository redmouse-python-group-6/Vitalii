from django.conf.urls import url
from article import views as article_views
urlpatterns = [
    url(r'^(?P<id>\w+)/$', article_views.get_article, name='get_article'),
    url(r'^(?P<text>\w+)/(?P<id>\w+)/$', article_views.get_article),
]
