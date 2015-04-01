#coding:utf-8
from django.views.generic import View
from django.shortcuts import get_object_or_404


def _add_page_view(func):
    def add(request, *args, **kwargs):
        obj = get_object_or_404(request.model, **kwargs)
        if hasattr(obj, "add_page_view"):
            obj.add_page_view()
        return func(request, *args, **kwargs)
    return add


class AddPageViewMixin(View):
    """
    注意：该mixin会与django-braces的mixin相冲突
    因为braces也是重写了dispatch()
    注意：该mixin仅适用于pk或id等直接定位obj的视图，如detailview
    """
    @_add_page_view
    def dispatch(self, request, *args, **kwargs):
        return super(AddPageViewMixin, self).dispatch(request, *args, **kwargs)