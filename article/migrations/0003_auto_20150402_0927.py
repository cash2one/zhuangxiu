# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import easy_thumbnails.fields


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0002_auto_20150331_1346'),
    ]

    operations = [
        migrations.AddField(
            model_name='type',
            name='keyword',
            field=models.CharField(max_length=40, null=True, verbose_name='\u5173\u952e\u8bcd', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='article',
            name='thumbnail',
            field=easy_thumbnails.fields.ThumbnailerImageField(upload_to=b'article', null=True, verbose_name='\u7f29\u7565\u56fe', blank=True),
        ),
    ]
