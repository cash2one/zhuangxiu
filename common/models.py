#coding:utf-8
import random
import datetime

from django.db import models
from django.contrib.sites.models import Site


# Create your models here.


class _CommonManager(models.Manager):

    def allow(self):
        return self.get_queryset().filter(allow=True)


class CommonModel(models.Model):
    page_view = models.IntegerField(u'查看数', default=0, blank=True, null=True)
    add_date = models.DateTimeField(u'加入时间', blank=True, null=True)
    order = models.IntegerField(u'排序', default=9999, blank=True, null=True)
    allow = models.NullBooleanField(u'审核?', default=True, blank=True, null=True)

    objects = _CommonManager()

    class Meta:
        abstract = True

    def get_full_url(self):
        return "http://%s%s" % (Site.objects.get_current().domain, self.get_absolute_url())

    def add_page_view(self):
        self.page_view += 1
        self.save()

    def save(self, *args, **kwargs):
        if not self.add_date:
            self.add_date = datetime.datetime.now()
        return super(CommonModel, self).save(*args, **kwargs)

