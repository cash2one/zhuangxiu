# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import taggit.managers
import easy_thumbnails.fields


class Migration(migrations.Migration):

    dependencies = [
        ('taggit', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Gallery',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('page_view', models.IntegerField(default=0, null=True, verbose_name='\u67e5\u770b\u6570', blank=True)),
                ('add_date', models.DateTimeField(null=True, verbose_name='\u52a0\u5165\u65f6\u95f4', blank=True)),
                ('order', models.IntegerField(default=9999, null=True, verbose_name='\u6392\u5e8f', blank=True)),
                ('allow', models.NullBooleanField(default=True, verbose_name='\u5ba1\u6838?')),
                ('title', models.CharField(max_length=50, verbose_name='\u6807\u9898')),
                ('describe', models.TextField(null=True, verbose_name='\u63cf\u8ff0', blank=True)),
                ('tags', taggit.managers.TaggableManager(to='taggit.Tag', through='taggit.TaggedItem', blank=True, help_text='\u8bf7\u8f93\u5165\u82f1\u6587\u6807\u7b7e\uff0c\u5e76\u7528\u82f1\u6587\u9017\u53f7\u5206\u9694\u591a\u4e2a\u6807\u7b7e', verbose_name='\u6807\u7b7e')),
            ],
            options={
                'verbose_name': '\u76f8\u518c',
                'verbose_name_plural': '\u76f8\u518c',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='GalleryUpload',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('zip', models.FileField(help_text='\u8bf7\u4e0a\u4f20.zip\u6587\u4ef6,\u56fe\u7247\u4e0d\u80fd\u5305\u542b\u5728\u6587\u4ef6\u5939\u91cc', upload_to=b'gallery/20150326', verbose_name='zip\u6587\u4ef6')),
                ('title', models.CharField(max_length=50, null=True, verbose_name='\u6807\u9898', blank=True)),
                ('describe', models.TextField(verbose_name='\u63cf\u8ff0', blank=True)),
                ('gallery', models.ForeignKey(blank=True, to='gallery.Gallery', help_text='\u9009\u62e9\u76f8\u518c\u5219\u4e3a\u8be5\u76f8\u518c\u6dfb\u52a0\u56fe\u7247\uff0c\u7559\u7a7a\u5219\u65b0\u5efa\u76f8\u518c', null=True, verbose_name='\u76f8\u518c')),
            ],
            options={
                'verbose_name': '\u6279\u91cf\u4e0a\u4f20',
                'verbose_name_plural': '\u6279\u91cf\u4e0a\u4f20',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Photo',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('page_view', models.IntegerField(default=0, null=True, verbose_name='\u67e5\u770b\u6570', blank=True)),
                ('add_date', models.DateTimeField(null=True, verbose_name='\u52a0\u5165\u65f6\u95f4', blank=True)),
                ('order', models.IntegerField(default=9999, null=True, verbose_name='\u6392\u5e8f', blank=True)),
                ('allow', models.NullBooleanField(default=True, verbose_name='\u5ba1\u6838?')),
                ('title', models.CharField(max_length=50, null=True, verbose_name='\u6807\u9898', blank=True)),
                ('image', easy_thumbnails.fields.ThumbnailerImageField(upload_to=b'gallery/20150326', null=True, verbose_name='\u56fe\u7247', blank=True)),
                ('describe', models.TextField(null=True, verbose_name='\u63cf\u8ff0', blank=True)),
                ('gallery', models.ForeignKey(verbose_name='\u76f8\u518c', blank=True, to='gallery.Gallery', null=True)),
                ('tags', taggit.managers.TaggableManager(to='taggit.Tag', through='taggit.TaggedItem', blank=True, help_text='\u8bf7\u8f93\u5165\u82f1\u6587\u6807\u7b7e\uff0c\u5e76\u7528\u82f1\u6587\u9017\u53f7\u5206\u9694\u591a\u4e2a\u6807\u7b7e', verbose_name='\u6807\u7b7e')),
            ],
            options={
                'verbose_name': '\u56fe\u7247',
                'verbose_name_plural': '\u56fe\u7247',
            },
            bases=(models.Model,),
        ),
    ]
