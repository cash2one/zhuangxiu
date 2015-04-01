#coding:utf-8
__author__ = 'chenwenlin'
from django.contrib.sites.models import Site
from django import template
from django.core.urlresolvers import reverse


register = template.Library()


@register.simple_tag()
def generate_gallery_url(photo=None):
    if not photo:
        return "javascript:void(0);"
    else:
        url = reverse('gallery:detail', args=[photo])
        return "http://%s%s" % (Site.objects.get_current().domain, url)


@register.simple_tag()
def generate_filter_url(room='all', style='all', photo=None):
    if not photo:
        return "javascript:void(0);"
    else:
        url = reverse('gallery:filter-detail', args=[room, style, photo])
        return "http://%s%s" % (Site.objects.get_current().domain, url)


