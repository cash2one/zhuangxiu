__author__ = 'Administrator'
from django.conf.urls import url, patterns
from .views import *


urlpatterns = patterns('',
    url(r'^$', GalleryListView.as_view(), name='list'),
    url(r'^photo-(?P<photo>\d+).html/$', GalleryDetailView.as_view(), name='detail'),
    url(r'^(?P<room>\w+)-(?P<style>\w+).html/$', PhotoListView.as_view(), name='filter'),
    url(r'^(?P<room>\w+)-(?P<style>\w+)/(?P<photo>\d+).html/$', PhotoDetailView.as_view(), name='filter-detail'),
)
