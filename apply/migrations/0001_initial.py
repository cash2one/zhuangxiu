# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Apply',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('page_view', models.IntegerField(default=0, null=True, verbose_name='\u67e5\u770b\u6570', blank=True)),
                ('add_date', models.DateTimeField(null=True, verbose_name='\u52a0\u5165\u65f6\u95f4', blank=True)),
                ('order', models.IntegerField(default=9999, null=True, verbose_name='\u6392\u5e8f', blank=True)),
                ('allow', models.NullBooleanField(default=True, verbose_name='\u5ba1\u6838?')),
                ('name', models.CharField(max_length=20, verbose_name='\u59d3\u540d')),
                ('phone', models.CharField(max_length=11, verbose_name='\u624b\u673a')),
                ('type', models.CharField(max_length=20, verbose_name='\u7c7b\u578b')),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model,),
        ),
    ]
