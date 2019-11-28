from django.shortcuts import render
from django.http import HttpResponse,JsonResponse,FileResponse
from app_get_data.models import pacon_datas
from function.pacon_data.data_myaql_url import *
import json
import hashlib

def index_scetc_news(request):
    data = all_data_url()
    # print(data)
    # print(type(data))
    return JsonResponse(data, json_dumps_params={'ensure_ascii':False})

def json_test(request):
    data = data_url()
    # print(data)
    # print(type(data))
    return JsonResponse(data, json_dumps_params={'ensure_ascii':False})


def image(request):
    if request.method == 'POST':
        files = request.FILES
        print("@@@", files)
        response = []
        for key, value in files.items():
            content = value.read()
            md5 = hashlib.md5(content).hexdigest()
            path = os.path.join('D:/', md5 + 'jpg')
            with open(path, "wb") as f:
                f.write(content)
            response.append({
                'name': key,
                'md5': md5
            })
    return HttpResponse("2131")


class ImageView():
    def post(self, request):
        files = request.FILES
        print("@@@",files)
        response =[]
        for key, value in files.items():
            content = value.read()
            md5 = hashlib.md5(content).hexdigest()
            path = os.path.join('D:/', md5 + 'jpg')
            with open(path, "wb") as f:
                f.write(content)
            response.append({
                'name': key,
                'md5': md5
            })
        return JsonResponse(data={'a':"123"})
