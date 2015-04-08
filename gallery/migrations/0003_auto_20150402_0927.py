# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import easy_thumbnails.fields


class Migration(migrations.Migration):

    dependencies = [
        ('gallery', '0002_auto_20150331_1346'),
    ]

    operations = [
        migrations.AlterField(
            model_name='galleryupload',
            name='zip',
            field=models.FileField(help_text='\u8bf7\u4e0a\u4f20.zip\u6587\u4ef6,\u56fe\u7247\u4e0d\u80fd\u5305\u542b\u5728\u6587\u4ef6\u5939\u91cc', upload_to=b'gallery', verbose_name='zip\u6587\u4ef6'),
        ),
        migrations.AlterField(
            model_name='photo',
            name='image',
            field=easy_thumbnails.fields.ThumbnailerImageField(upload_to=b'gallery', null=True, verbose_name='\u56fe\u7247', blank=True),
        ),
    ]
