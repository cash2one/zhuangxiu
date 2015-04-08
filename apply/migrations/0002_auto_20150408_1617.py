# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('apply', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='apply',
            options={'verbose_name': '\u7528\u6237\u7533\u8bf7', 'verbose_name_plural': '\u7528\u6237\u7533\u8bf7'},
        ),
        migrations.AlterField(
            model_name='apply',
            name='type',
            field=models.IntegerField(help_text='0\u4e3a\u91cf\u623f,1\u4e3a\u8bbe\u8ba1,2\u4e3a\u62a5\u4ef7', verbose_name='\u7c7b\u578b'),
        ),
    ]
