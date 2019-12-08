from django.conf.urls import url
from django.contrib import admin
from news.views import search,article, articles, addcomment


urlpatterns = [
    url(r'^search/',search, name='search'),
    url(r'^news/all/$', articles, name='all'),
    url(r'^news/get/(?P<article_id>\d+)$', article),
    url(r'^news/addcomment/(?P<article_id>\d+)$', addcomment),
]