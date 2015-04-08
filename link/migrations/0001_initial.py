# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Link',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('page_view', models.IntegerField(default=0, null=True, verbose_name='\u67e5\u770b\u6570', blank=True)),
                ('add_date', models.DateTimeField(null=True, verbose_name='\u52a0\u5165\u65f6\u95f4', blank=True)),
                ('order', models.IntegerField(default=9999, null=True, verbose_name='\u6392\u5e8f', blank=True)),
                ('allow', models.NullBooleanField(default=True, verbose_name='\u5ba1\u6838?')),
                ('keyword', models.CharField(max_length=40, verbose_name='\u5173\u952e\u8bcd')),
                ('url', models.URLField(verbose_name='\u94fe\u63a5')),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model,),
        ),
    ]
