import os
from function.aiword.dictation import text_baidu
from django.http import HttpResponse, JsonResponse, FileResponse
from pyv05 import settings
import utils.response
from django.views import View   # 类视图继承的类


filePath = settings.IMAGES_DIR + "/resqut.jpg"

class aiword(View, utils.response.ResponseMixin):
    def get(self, request):
        '''
        :param request:
        :return:  识别结果
        '''
        data = text_baidu(filePath)
        response = self.wrap_json_response(data=data)
        return JsonResponse(data=response, safe=False)  # 不存在则返回json数据，数据的data为not file

