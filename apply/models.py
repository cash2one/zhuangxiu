#coding:utf-8
from django.db import models
from common.models import *
# Create your models here.


class Apply(CommonModel):
    name = models.CharField(u'姓名', max_length=20)
    phone = models.CharField(u'手机', max_length=11)
    type = models.IntegerField(u'类型', help_text=u'0为量房,1为设计,2为报价')

    def __unicode__(self):
        return self.name

    class Meta:
        verbose_name = u'用户申请'
        verbose_name_plural = verbose_name
