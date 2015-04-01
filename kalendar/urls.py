#coding:utf-8
__author__ = 'chenwenlin'
from django.conf.urls import url, patterns
from .views import *


urlpatterns = patterns('',
    url(r'^$', KalendarTemplateView.as_view(), name='index')
)
