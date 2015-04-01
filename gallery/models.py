#coding:utf-8

import zipfile
import os
from io import BytesIO
from PIL import Image
import datetime

from django.db import models
from django.core.files.storage import default_storage
from django.core.exceptions import ValidationError
from django.core.files.base import ContentFile

from easy_thumbnails.fields import ThumbnailerImageField
from easy_thumbnails.files import get_thumbnailer
from taggit.managers import TaggableManager

from common.models import CommonModel
# Create your models here.


class Gallery(CommonModel):
    title = models.CharField(u'标题', max_length=50)
    describe = models.TextField(verbose_name=u'描述', blank=True, null=True)

    class Meta:
        verbose_name = u'相册'
        verbose_name_plural = verbose_name

    def __unicode__(self):
        return self.title

    def admin_thumbnail(self):
        img = self.get_cover()
        if img:
            try:
                return '<img src="%s">' % get_thumbnailer(img.image)['10062'].url
            except IOError:
                return 'IOError'
        return u'空的相册'

    admin_thumbnail.short_description = u'封面'

    def get_cover(self):
        if self.photo_set.count() > 0:
            return self.photo_set.allow().order_by('order')[0]


class Photo(CommonModel):
    title = models.CharField(u'标题', max_length=50, blank=True, null=True)
    image = ThumbnailerImageField(u'图片', blank=True, null=True,upload_to='gallery')
    gallery = models.ForeignKey(Gallery, verbose_name=u'相册', blank=True, null=True)
    describe = models.TextField(u'描述', blank=True, null=True)
    tags = TaggableManager(verbose_name=u'标签', help_text=u'请输入英文标签，并用空格分隔多个标签',
                           blank=True)

    class Meta:
        verbose_name = u'图片'
        verbose_name_plural = verbose_name

    def __unicode__(self):
        return unicode(self.add_date)


class GalleryUpload(models.Model):
    zip = models.FileField(u'zip文件', help_text=u'请上传.zip文件,图片不能包含在文件夹里', upload_to='gallery')
    title = models.CharField(u'标题', blank=True, null=True, max_length=50)
    gallery = models.ForeignKey(Gallery, verbose_name=u'相册', null=True, blank=True,
                                help_text=u'选择相册则为该相册添加图片，留空则新建相册')
    describe = models.TextField(u'描述', blank=True)

    class Meta:
        verbose_name = u'批量上传'
        verbose_name_plural = verbose_name

    def clean(self):
        if not self.title and not self.gallery:
            raise ValidationError(u"请输入标题用来创建新相册或者选择一个已存在的相册添加图片")

    def save(self, *args, **kwargs):
        super(GalleryUpload, self).save(*args, **kwargs)
        gallery = self.process_zipfile()
        super(GalleryUpload, self).delete()
        return gallery

    def process_zipfile(self):
        if default_storage.exists(self.zip.name):
            zip_file = zipfile.ZipFile(default_storage.open(self.zip.name))
            bad_file = zip_file.testzip()
            if bad_file:
                zip_file.close()
                raise Exception(u"%s 文档是损坏的" % bad_file)
            if self.gallery:
                gallery = self.gallery
            else:
                gallery = Gallery.objects.create(title=self.title,
                                                 describe=self.describe)
            for filename in sorted(zip_file.namelist()):

                if filename.startswith('__') or filename.startswith('.'):
                    #忽略以 __和 .  开头的文件
                    continue

                if os.path.dirname(filename):
                    #图片不能放在文件夹里
                    continue

                data = zip_file.read(filename)

                if not len(data):
                    continue

                # Basic check that we have a valid image.
                try:
                    file = BytesIO(data)
                    opened = Image.open(file)
                    opened.verify()
                except Exception:
                    # Pillow (or PIL) doesn't recognize it as an image.
                    # If a "bad" file is found we just skip it.
                    # But we do flag this both in the logs and to the user.
                    continue

                content_file = ContentFile(data)
                photo = Photo(gallery=gallery)
                photo.image.save(filename, content_file)
                photo.save()

            zip_file.close()
            return gallery



