#coding:utf-8
from django.views.generic import *
from django.http import Http404

from .models import *

from common.mixins import AddPageViewMixin

# Create your views here.


class ArticleDetailView(AddPageViewMixin, DetailView):
    model = Article

    def get_object(self, queryset=None):
        try:
            obj = Article.objects.select_related('type').get(pk=self.kwargs["pk"])
        except Article.DoesNotExist:
            raise Http404
        return obj


class ArticleListView(ListView):
    model = Article

    def get_queryset(self):
        qs = Article.objects.allow().order_by('-add_date')
        if 'type' in self.kwargs:
            qs = qs.filter(type__short_title=self.kwargs["type"])
        return qs

    def get_context_data(self, **kwargs):
        if 'type' in self.kwargs:
            kwargs.update({"type": Type.objects.get(short_title=self.kwargs["type"])})
        return super(ArticleListView, self).get_context_data(**kwargs)


class HomeTemplateView(TemplateView):
    template_name = 'home.html'


class BuzhouTemplateView(TemplateView):
    template_name = 'article/buzhou.html'








