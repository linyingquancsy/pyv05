from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
import utils.response
from django.views import View   # 类视图继承的类
from indexs.models import iot_data
import os
import hashlib
from pyv05 import settings

data = {
    'tem': "#",
    'hum': "#",
    'somken': "#",
    'mea': "#",
    'door': "#",
    'winzhu': "#",
    'winci': "#",
    'people': "#",
    'cpu': "#"
}
data1 = {
    'tem': "#",
    'hum': "#",
    'somken': "#",
    'mea': "#",
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
    # 查询数据库
    user = iot_data.objects.using('iot').order_by('id').reverse()
    print("所有数据", user)
    print("len", len(user))
    print("所有数据", user[0].tem)
    for i in range(len(data)):
        data1['tem'] = user[0].tem
        data1['hum'] = user[0].hum
        data1['somken'] = user[0].somken
        data1['mea'] = user[0].mea
        data1['door'] = user[0].door
        data1['winzhu'] = user[0].winzhu
        data1['winci'] = user[0].winci
        data1['people'] = user[0].people
        data1['cpu'] = user[0].cpu
    data_iot = data1
    # if len(user) > 10:
    #     iot_data.objects.using('iot').all().delete()
    #     print("定期删除完成")
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
        new_user_list = []
        # print(str(files, encoding="utf-8"))
        text_data = str(files, encoding="utf-8").replace("=", "&").split("&")
        for i in range(0, len(text_data), 2):
            data[text_data[i]] = text_data[i+1]
        print("字典数据", data)
        # 存入数据库
        data_test = iot_data(tem=data['tem'], hum=data['hum'], somken=data['somken'], mea=data['mea'], door=data['door'], winzhu=data['winzhu'], winci=data['winci'], people=data['people'], cpu=data['cpu'])
        data_test.save(using='iot')
        print("数据存入数据库成功！")

        message = 'post'
        response_json = self.wrap_json_response(data=response, code='Success', message=message)
        return JsonResponse(data=response_json, safe=False)
