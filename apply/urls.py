__author__ = 'chenwenlin'
from django.conf.urls import url, patterns
from .views import *


urlpatterns = patterns('',
    url(r'^create.html/$', ApplyCreateView.as_view(), name='create'),
)