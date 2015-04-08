#coding:utf-8
from django.contrib import admin
from .models import *
# Register your models here.


class LinkAdmin(admin.ModelAdmin):
    fieldsets = (
        (None, {
            'fields': ('keyword', 'url')
        }),
        (u'高级选项',{
            'classes': ('collapse',),
            'fields': ('allow', 'page_view', 'order', 'add_date')
        })
    )
    list_display = ('keyword', 'url', 'add_date')
    list_filter = ('add_date', 'allow')

admin.site.register(Link, LinkAdmin)
