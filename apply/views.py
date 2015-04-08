#coding:utf-8
import datetime
from django.views.generic import CreateView
from braces.views import JSONResponseMixin
from .models import *
# Create your views here.


class ApplyCreateView(JSONResponseMixin, CreateView):
    http_method_names = [u'post']
    model = Apply
    fields = ('name', 'phone', 'type')

    def form_valid(self, form):
        if Apply.objects.filter(add_date__gt=datetime.datetime.today(), phone=form.cleaned_data["phone"]).exists():
            result = False
            msg = u"您已经提交过了,请耐心等待我们的管理员与您联系。"
        else:
            result = True
            msg = u"提交成功,我们的工作人员将会马上联系您。"
            self.object = form.save()
        return self.render_json_response({"result": result, "msg": msg})

