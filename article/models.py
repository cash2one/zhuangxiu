#coding:utf-8

from django.db import models
from django.contrib.auth.models import User
from django.utils.html import strip_tags
from django.core.urlresolvers import reverse


from DjangoUeditor.models import UEditorField
from easy_thumbnails.fields import ThumbnailerImageField
from taggit.managers import TaggableManager

from common.models import CommonModel


class Type(models.Model):
    title = models.CharField(u'类型', max_length=40)
    short_title = models.CharField(u'缩写', max_length=20)
    parent = models.ForeignKey('self', verbose_name=u'父类', blank=True, null=True)

    class Meta:
        verbose_name = u'文章类型'
        verbose_name_plural = verbose_name

    def __unicode__(self):
        return self.title


class Push(models.Model):
    title = models.CharField(u'名称', max_length=20)
    short_title = models.CharField(u'缩写', max_length=20)

    def __unicode__(self):
        return self.title

    class Meta:
        verbose_name = u'推送类别'
        verbose_name_plural = verbose_name


class Article(CommonModel):
    title = models.CharField(u'标题', max_length=50)
    type = models.ForeignKey(Type, verbose_name=u"类别")
    user = models.ForeignKey(User, verbose_name=u"责任编辑")
    thumbnail = ThumbnailerImageField(u'缩略图', blank=True, null=True, upload_to='article')
    video = models.FileField(u'相关视频', upload_to='video', blank=True, null=True, help_text=u'此项必须上传缩略图')
    content = UEditorField(u'内容', blank=True, null=True, width=1000, height=500,
                           imagePath="article/%(year)s%(month)s%(day)s/%(datetime)s_%(rnd)s.%(extname)s")
    tags = TaggableManager(verbose_name=u'标签', help_text=u'请输入英文标签，并用空格分隔多个标签', blank=True)
    push = models.ForeignKey(Push, verbose_name=u'推送至', blank=True, null=True)
    url = models.URLField(u'链接地址', blank=True, null=True)

    class Meta:
        verbose_name = u'文章'
        verbose_name_plural = verbose_name

    def get_absolute_url(self):
        return reverse('article:detail', args=[self.pk])

    def __unicode__(self):
        return self.title

    def get_clean_content(self):
        """
        获得不含空格及HTML标签的干净的内容
        """
        content = strip_tags(self.content)
        content = content.replace("&nbsp;", "")
        return content







