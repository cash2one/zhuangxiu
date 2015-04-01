#coding:utf-8
from django.contrib import admin
from .models import *
# Register your models here.


class ArticleAdmin(admin.ModelAdmin):
    fieldsets = (
        (None, {
            'fields':('title', 'type', 'thumbnail', 'video', 'content', 'tags', 'push')
        }),
        (u'高级选项',{
            'classes': ('collapse',),
            'fields':('url', 'allow', 'page_view', 'order', 'add_date')
        })
    )
    radio_fields = {"type": admin.HORIZONTAL, 'push': admin.HORIZONTAL}
    list_display = ('title', 'allow', 'order', 'id')
    search_fields = ('title', 'content')
    list_editable = ('allow',  'order')
    list_filter = ('type', 'push', 'add_date', 'allow')

    def save_model(self, request, obj, form, change):
        obj.user = request.user
        obj.save()

admin.site.register(Type)
admin.site.register(Push)
admin.site.register(Article, ArticleAdmin)
