from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
import utils.response
from django.views import View   # 类视图继承的类
import os
import hashlib
from pyv05 import settings

data = {
    'tem': "#",
    'hum': "#",
    'somken': "#",
    'mea': "#",
    'light': "#",
    'door': "#",
    'winzhu': "#",
    'winci': "#",
    'people': "#",
    'cpu': "#"
}

# Create your views here.
def index(request):
    text = "目前只开发了几个小程序接口，后续会开发更多web应用，敬请期待！！！"
    return HttpResponse(text)

def iot_sensor(request):
    data_iot = data
    return JsonResponse(data_iot)

class api_iot(View, utils.response.ResponseMixin):
    def post(self, request):
        '''
        :param request:
        :return:
        '''
        files = request.body               # 接收客户端上传上来的数据（如微信小程序中的wx.uploadFile() Post方法的）
        # print('$$$', type(files))
        response = []
        # print(str(files, encoding="utf-8"))
        text_data = str(files, encoding="utf-8").replace("=", "&").split("&")
        for i in range(0, len(text_data), 2):
            data[text_data[i]] = text_data[i+1]
        # print(data)
        message = 'post'
        response_json = self.wrap_json_response(data=response, code='Success', message=message)
        return JsonResponse(data=response_json, safe=False)  # 返回json格式的数据，为图片名字，和md5
