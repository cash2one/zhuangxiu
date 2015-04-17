#coding:utf-8
import urllib
import urllib2

from django.core.mail import send_mail
from django.utils.http import urlquote
from django.views.generic import CreateView
from braces.views import JSONResponseMixin
from .models import *
# Create your views here.


class ApplyCreateView(JSONResponseMixin, CreateView):
    http_method_names = [u'post']
    model = Apply
    fields = ('name', 'phone', 'type')

    def form_valid(self, form):
        cleaned_data = form.cleaned_data
        if Apply.objects.filter(add_date__gt=datetime.datetime.today(), phone=cleaned_data["phone"]).exists():
            result = False
            msg = u"您已经提交过了,请耐心等待我们的管理员与您联系。"
        else:
            result = True
            msg = u"提交成功,我们的工作人员将会马上联系您。"
            self.object = form.save()
            type = cleaned_data["type"]
            if type == 0:
                type = u'量房'
            elif type == 1:
                type = u'设计'
            else:
                type = u'报价'
            content = u'姓名:%s,手机:%s,类型:%s' % (cleaned_data['name'], cleaned_data['phone'], type)
            send_mail(content, content, '598562755@qq.com', ['234814120@qq.com'], fail_silently=False)
            tpl_value = "#name#=%s" % (urlquote(cleaned_data['name']), )
            data = {"key": "77d43d39c7e12b92f089195f483a440d", "dtype": "json", "mobile": cleaned_data['phone'],
                    "tpl_id": "2374", "tpl_value": tpl_value}
            post = urllib.urlencode(data)
            url = "http://v.juhe.cn/sms/send"
            urllib2.urlopen(url, post)
        return self.render_json_response({"result": result, "msg": msg})


