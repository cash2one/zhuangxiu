#coding:utf-8
from django.contrib import admin
from django.core.cache import cache

from taggit.models import Tag, TaggedItem
from taggit.admin import TagAdmin
# Register your models here.


class NewTagAdmin(TagAdmin):
    """
    继承并添加taggit的action方法
    """

    actions = ['delete_no_quote', ]

    def delete_no_quote(self, request, queryset):
        item_cache = cache.get('item_list')
        if not item_cache:
            item_dict = TaggedItem.objects.select_related('tag').only("tag").values("tag").distinct()
            item_list = [item["tag"] for item in item_dict]
            cache.set('item_list', item_list)
            item_cache = item_list
        count = 0
        for query in queryset:
            if query.id not in item_cache:
                count += 1
                query.delete()

        self.message_user(request, u'成功删除 %s个 没被引用的tag' % count)


admin.site.unregister(Tag)
admin.site.register(Tag, NewTagAdmin)