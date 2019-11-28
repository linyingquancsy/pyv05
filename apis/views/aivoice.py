import os
from function.aiword.voice import result_mp3
from function.aiword.dictation import text_baidu
from django.http import HttpResponse, JsonResponse, FileResponse
from pyv05 import settings
import utils.response
import json
import base64
from django.views import View   # 类视图继承的类
import time
filePath = settings.IMAGES_DIR + "\\resqut.jpg"
datalist = {}



class aivoice(View, utils.response.ResponseMixin):
    def get(self, request):
        '''
        :param request:
        :return:  读音
        '''
        # print(text_baidu(filePath))
        listdata = text_baidu(filePath)
        print(listdata)
        for i in range(len(listdata)):
            datalist[i] = result_mp3(listdata[i])
        return HttpResponse('数据已经保存！')


class voicePlay(View, utils.response.ResponseMixin):
    def get(self, request):
        header = int(request.META.get("HTTP_SUM"))
        print("header", header)
        print(datalist[header])
        return HttpResponse(datalist[header])

def file_content(filePath):
    with open(filePath, 'rb') as fp:
        return fp.read()

class filevoice(View):
    def get(self, request):
        data = file_content(settings.IMAGES_DIR + "\\result.mp3")
        print('data', data)
        return FileResponse(data)