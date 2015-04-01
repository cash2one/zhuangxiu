#coding:utf-8
from django.contrib import admin
from .models import *

# Register your models here.




class PhotoAdmin(admin.ModelAdmin):
    fieldsets = (
        (None, {
            'fields': ('title', 'image', 'gallery', 'describe', 'tags')
        }),
        (u'高级选项',{
            'classes': ('collapse',),
            'fields': ('page_view', 'allow', 'order', 'add_date')
        })
    )

admin.site.register(Photo, PhotoAdmin)


class InlinePhotoAdmin(admin.TabularInline):
    model = Photo
    fieldsets = ((None, {'fields': ['image', 'title', 'order', 'tags']}),)


class GalleryAdmin(admin.ModelAdmin):
    fieldsets = (
        (None, {
            'fields': ('title', 'describe', 'tags')
        }),
        (u'高级选项',{
            'classes': ('collapse',),
            'fields': ('page_view', 'allow', 'order', 'add_date')
        })
    )
    list_display = ('admin_thumbnail', 'title', 'allow', 'order')
    list_editable = ('allow', 'order')
    inlines = [InlinePhotoAdmin]

admin.site.register(Gallery, GalleryAdmin)

admin.site.register(GalleryUpload)