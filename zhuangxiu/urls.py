from django.conf.urls import patterns, include, url
from django.contrib import admin

from article.views import HomeTemplateView, BuzhouTemplateView

import settings

urlpatterns = patterns('',
    url(r'^gallery/', include('gallery.urls', namespace='gallery')),
    url(r'^article/', include('article.urls', namespace='article')),
    url(r'^kalendar/', include('kalendar.urls', namespace='kalendar')),
    url(r'^apply/', include('apply.urls', namespace='apply')),
    url(r'^ueditor/',include('DjangoUeditor.urls')),
    url(r'^$', HomeTemplateView.as_view(), name='home'),
    url(r'^buzhou.html/$', BuzhouTemplateView.as_view(), name='buzhou'),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^media/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.MEDIA_ROOT}),
)
