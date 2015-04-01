# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import taggit.managers
import easy_thumbnails.fields


class Migration(migrations.Migration):

    dependencies = [
        ('gallery', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='gallery',
            name='tags',
        ),
        migrations.AlterField(
            model_name='galleryupload',
            name='zip',
            field=models.FileField(help_text='\u8bf7\u4e0a\u4f20.zip\u6587\u4ef6,\u56fe\u7247\u4e0d\u80fd\u5305\u542b\u5728\u6587\u4ef6\u5939\u91cc', upload_to=b'gallery/20150331', verbose_name='zip\u6587\u4ef6'),
        ),
        migrations.AlterField(
            model_name='photo',
            name='image',
            field=easy_thumbnails.fields.ThumbnailerImageField(upload_to=b'gallery/20150331', null=True, verbose_name='\u56fe\u7247', blank=True),
        ),
        migrations.AlterField(
            model_name='photo',
            name='tags',
            field=taggit.managers.TaggableManager(to='taggit.Tag', through='taggit.TaggedItem', blank=True, help_text='\u8bf7\u8f93\u5165\u82f1\u6587\u6807\u7b7e\uff0c\u5e76\u7528\u7a7a\u683c\u5206\u9694\u591a\u4e2a\u6807\u7b7e', verbose_name='\u6807\u7b7e'),
        ),
    ]
