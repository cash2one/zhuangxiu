#coding:utf-8
__author__ = 'chenwenlin'


from django.core.files.storage import FileSystemStorage
from django.conf import settings
import os
import time
import random


class FileStorage(FileSystemStorage):
    def __init__(self, location=settings.MEDIA_ROOT, base_url=settings.MEDIA_URL):
        #初始化
        super(FileStorage, self).__init__(location, base_url)

    #重写 _save方法
    def _save(self, name, content):
        #文件扩展名
        ext = os.path.splitext(name)[1]
        #文件目录
        d = os.path.join(os.path.dirname(name), time.strftime("%Y%m%d"))
        #定义文件名，年月日时分秒随机数
        fn = "%s%s%s%s" % (time.strftime("%Y%m%d%H%M%S"), random.choice('abcdefghijklmnopqrsduvwsyz'),
                           random.randint(1000, 9999), random.choice('abcdefghijklmnopqrsduvwsyz'))
        #重写合成文件名
        name = os.path.join(d, fn + ext)
        #调用父类方法
        return super(FileStorage, self)._save(name, content)