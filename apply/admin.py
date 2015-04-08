#coding:utf-8
from django.contrib import admin
from .models import *
# Register your models here.


class ApplyAdmin(admin.ModelAdmin):
    fieldsets = (
        (None, {
            'fields': ('name', 'phone', 'type')
        }),
        (u'高级选项',{
            'classes': ('collapse',),
            'fields': ('allow', 'page_view', 'order', 'add_date')
        })
    )
    list_display = ('name', 'phone', 'type', 'add_date')
    list_filter = ('add_date', 'allow')

admin.site.register(Apply, ApplyAdmin)