#coding:utf-8
from django.db import models
from common.models import CommonModel
# Create your models here.


class Link(CommonModel):
    keyword = models.CharField(u'关键词', max_length=40)
    url = models.URLField(u'链接')

    def __unicode__(self):
        return self.keyword

    class Meta:
        verbose_name = u'友情链接'
        verbose_name_plural = verbose_name
