# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import easy_thumbnails.fields
import DjangoUeditor.models
from django.conf import settings
import taggit.managers


class Migration(migrations.Migration):

    dependencies = [
        ('taggit', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('page_view', models.IntegerField(default=0, null=True, verbose_name='\u67e5\u770b\u6570', blank=True)),
                ('add_date', models.DateTimeField(null=True, verbose_name='\u52a0\u5165\u65f6\u95f4', blank=True)),
                ('order', models.IntegerField(default=9999, null=True, verbose_name='\u6392\u5e8f', blank=True)),
                ('allow', models.NullBooleanField(default=True, verbose_name='\u5ba1\u6838?')),
                ('title', models.CharField(max_length=50, verbose_name='\u6807\u9898')),
                ('thumbnail', easy_thumbnails.fields.ThumbnailerImageField(upload_to=b'article/20150326', null=True, verbose_name='\u7f29\u7565\u56fe', blank=True)),
                ('video', models.FileField(help_text='\u6b64\u9879\u5fc5\u987b\u4e0a\u4f20\u7f29\u7565\u56fe', upload_to=b'video', null=True, verbose_name='\u76f8\u5173\u89c6\u9891', blank=True)),
                ('content', DjangoUeditor.models.UEditorField(null=True, verbose_name='\u5185\u5bb9', blank=True)),
                ('url', models.URLField(null=True, verbose_name='\u94fe\u63a5\u5730\u5740', blank=True)),
            ],
            options={
                'verbose_name': '\u6587\u7ae0',
                'verbose_name_plural': '\u6587\u7ae0',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Push',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=20, verbose_name='\u540d\u79f0')),
                ('short_title', models.CharField(max_length=20, verbose_name='\u7f29\u5199')),
            ],
            options={
                'verbose_name': '\u63a8\u9001\u7c7b\u522b',
                'verbose_name_plural': '\u63a8\u9001\u7c7b\u522b',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Type',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=40, verbose_name='\u7c7b\u578b')),
                ('short_title', models.CharField(max_length=20, verbose_name='\u7f29\u5199')),
                ('parent', models.ForeignKey(verbose_name='\u7236\u7c7b', blank=True, to='article.Type', null=True)),
            ],
            options={
                'verbose_name': '\u6587\u7ae0\u7c7b\u578b',
                'verbose_name_plural': '\u6587\u7ae0\u7c7b\u578b',
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='article',
            name='push',
            field=models.ForeignKey(verbose_name='\u63a8\u9001\u81f3', blank=True, to='article.Push', null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='article',
            name='tags',
            field=taggit.managers.TaggableManager(to='taggit.Tag', through='taggit.TaggedItem', blank=True, help_text='\u8bf7\u8f93\u5165\u82f1\u6587\u6807\u7b7e\uff0c\u5e76\u7528\u82f1\u6587\u9017\u53f7\u5206\u9694\u591a\u4e2a\u6807\u7b7e', verbose_name='\u6807\u7b7e'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='article',
            name='type',
            field=models.ForeignKey(verbose_name='\u7c7b\u522b', to='article.Type'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='article',
            name='user',
            field=models.ForeignKey(verbose_name='\u8d23\u4efb\u7f16\u8f91', to=settings.AUTH_USER_MODEL),
            preserve_default=True,
        ),
    ]
