from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def index(request):
    text = "目前只开发了几个小程序接口，后续会开发更多web应用，敬请期待！！！"
    return HttpResponse(text)