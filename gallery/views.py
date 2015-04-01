#coding:utf-8
from django.shortcuts import render
from django.views.generic import *
from django.db.models import Q, F
from .models import *


# Create your views here.
def get_photo_detail(photo_list, photo):
    match = False
    temp = None
    count = 1
    photo.previous_photo = None
    photo.next_photo = None
    photo.current_num = 1
    photo.total_num = photo_list.count()
    for p in photo_list:
        if match:
            #说明在上一个p时，已经被证实当前photo
            photo.next_photo = p
            break
        if p == photo:
            #此时temp仍存储的是上一个p
            photo.previous_photo = temp
            photo.current_num = count
            match = True
        temp = p
        count += 1
    return photo


class GalleryListView(ListView):
    model = Gallery

    def get_queryset(self):
        gallery = Gallery.objects.allow().order_by('order')
        return gallery


class GalleryDetailView(DetailView):
    model = Photo
    template_name = 'gallery/gallery_detail.html'

    def get_object(self, queryset=None):
        photo = Photo.objects.select_related("gallery").get(id=self.kwargs["photo"])
        photo_list = photo.gallery.photo_set.allow().order_by('order')
        photo = get_photo_detail(photo_list, photo)
        return photo


class PhotoListView(ListView):
    model = Photo

    def get_queryset(self):
        photo_list = Photo.objects.allow()
        if 'room' in self.kwargs:
            room = self.kwargs["room"]
            if not room == 'all':
                photo_list = photo_list.filter(tags__name__in=(room,))
        if 'style' in self.kwargs:
            style = self.kwargs["style"]
            if not style == 'all':
                photo_list = photo_list.filter(tags__name__in=(style,))
        return photo_list


class PhotoDetailView(DetailView):
    model = Photo

    def get_object(self, queryset=None):
        photo = Photo.objects.select_related("gallery").get(id=self.kwargs["photo"])
        photo_list = Photo.objects.allow()
        if 'room' in self.kwargs:
            room = self.kwargs["room"]
            if not room == 'all':
                photo_list = photo_list.filter(tags__name__in=(room,))
        if 'style' in self.kwargs:
            style = self.kwargs["style"]
            if not style == 'all':
                photo_list = photo_list.filter(tags__name__in=(style,))
        photo = get_photo_detail(photo_list, photo)
        return photo



