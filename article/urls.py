__author__ = 'Administrator'
from django.conf.urls import url, patterns
from .views import *

urlpatterns = patterns('',
    url(r'^$', ArticleListView.as_view(), name='index'),
    url(r'^(?P<pk>\d+).html/$', ArticleDetailView.as_view(), name='detail'),
    url(r'^(?P<type>\w+).html/$', ArticleListView.as_view(), name='list'),
)
