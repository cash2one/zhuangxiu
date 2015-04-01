#coding:utf-8
__author__ = 'Administrator'
from django import template

from classytags.helpers import InclusionTag
from classytags.core import Options
from classytags.arguments import Argument

from ..models import *

register = template.Library()


class show_article_related(InclusionTag):
    """
    获得相关文章
    template：模板名，需完整路径
    tags：django-taggit
    length：提取的长度
    """
    options = Options(
        Argument('template', resolve=True),
        Argument('tags', resolve=True),
        Argument('length', resolve=True)
    )

    def get_template(self, context, **kwargs):
        template = kwargs["template"]
        return template

    def get_context(self, context, **kwargs):
        tags = kwargs["tags"]
        length = int(kwargs["length"])
        list = tags.similar_objects()[:length]
        return {"list": list}
register.tag(show_article_related)







