from django.shortcuts import render
from django.views.generic import *
# Create your views here.


class KalendarTemplateView(TemplateView):
    template_name = 'kalendar/kalendar_list.html'