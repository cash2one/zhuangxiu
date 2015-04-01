#coding:utf-8
__author__ = 'Administrator'
import random

from django import template
from django.db.models.loading import get_model
from django.core.urlresolvers import reverse
from django.contrib.sites.models import Site

from classytags.helpers import InclusionTag
from classytags.core import Options
from classytags.arguments import Argument

register = template.Library()


class show_list(InclusionTag):
    """
    获得文章列表
    template：模板名，需完整路径
    app: app名
    model： 类名
    type：type外键
    order： 排序参数
    length：提取的长度
    """
    options = Options(
        Argument('template', resolve=True),
        Argument('app', resolve=True),
        Argument('model', resolve=True),
        Argument('type', resolve=True),
        Argument('order', resolve=True),
        Argument('length', resolve=True)
    )

    def get_template(self, context, **kwargs):
        template = kwargs["template"]
        return template

    def get_context(self, context, **kwargs):
        app = kwargs["app"]
        model = kwargs["model"]
        type = kwargs["type"]
        order = kwargs["order"]
        length = int(kwargs["length"])
        current = get_model(app, model)
        if type == "all":
            list = current.objects.allow().order_by(order)[:length]
        else:
            list = current.objects.allow().filter(type__short_title=type).order_by(order)[:length]
        return {"list": list}
register.tag(show_list)


class show_random(InclusionTag):
    """
    获得随机文章列表
    template：模板名，需完整路径
    app: app名
    model： 类名
    type：type外键
    length：提取的长度
    """
    options = Options(
        Argument('template', resolve=True),
        Argument('app', resolve=True),
        Argument('model', resolve=True),
        Argument('type', resolve=True),
        Argument('length', resolve=True)
    )

    def get_template(self, context, **kwargs):
        template = kwargs["template"]
        return template

    def get_context(self, context, **kwargs):
        app = kwargs["app"]
        model = kwargs["model"]
        type = kwargs["type"]
        length = int(kwargs["length"])
        current = get_model(app, model)
        count = current.objects.filter(type__short_title=type).count()
        list = []
        if count > length:
            num = random.randint(length, count)
            list = current.objects.allow().filter(type__short_title=type)[num-length:num]
        return {"list": list}
register.tag(show_random)


class show_push(InclusionTag):
    """
    获得推送文章
    template：模板名，需完整路径
    app: app名
    model：类名
    push：push参数
    length：提取的长度
    """
    options = Options(
        Argument('template', resolve=True),
        Argument('app', resolve=True),
        Argument('model', resolve=True),
        Argument('push', resolve=True),
        Argument('length', resolve=True)
    )

    def get_template(self, context, **kwargs):
        template = kwargs["template"]
        return template

    def get_context(self, context, **kwargs):
        app = kwargs["app"]
        model = kwargs["model"]
        push = kwargs["push"]
        length = int(kwargs["length"])
        current = get_model(app, model)
        list = current.objects.allow().filter(push__short_title=push).order_by("-add_date")[:length]
        return {"list": list}
register.tag(show_push)



@register.simple_tag()
def show_full_url(module, *args):
    if len(args) == 0:
        url = reverse(module)
    else:
        url = reverse(module, args=args)
    return "http://%s%s" % (Site.objects.get_current().domain, url)