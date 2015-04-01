# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import taggit.managers
import easy_thumbnails.fields


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='tags',
            field=taggit.managers.TaggableManager(to='taggit.Tag', through='taggit.TaggedItem', blank=True, help_text='\u8bf7\u8f93\u5165\u82f1\u6587\u6807\u7b7e\uff0c\u5e76\u7528\u7a7a\u683c\u5206\u9694\u591a\u4e2a\u6807\u7b7e', verbose_name='\u6807\u7b7e'),
        ),
        migrations.AlterField(
            model_name='article',
            name='thumbnail',
            field=easy_thumbnails.fields.ThumbnailerImageField(upload_to=b'article/20150331', null=True, verbose_name='\u7f29\u7565\u56fe', blank=True),
        ),
    ]
