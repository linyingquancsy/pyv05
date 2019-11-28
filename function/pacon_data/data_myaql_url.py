# -*- coding: UTF-8 -*-
import os
import django
import json
from collections import defaultdict
# 创建Django环境
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'pyv03.settings')
django.setup()
from app_get_data.models import pacon_datas

def data_url():
    '''
    取出数据库部分数据
    :return: 所有数据库数据（json格式）
    '''
    data = {}
    datas = {}
    res = defaultdict(dict)
    data_title = pacon_datas.objects.values()
    data['list'] = list(data_title)
    for i in range(len(data_title)):
        datas[i] = data['list'][i]
    for m in range(len(data_title)):
        res[m]['title'] = datas[m]['title_news']
        res[m]['time'] = datas[m]['times_news']
        res[m]['read'] = datas[m]['reads_news']

    reads = dict(res)
    return reads

def all_data_url():
    '''
    取出数据库部分数据
    :return: 所有数据库数据（json格式）
    '''
    data = {}
    datas = {}
    res = defaultdict(dict)
    data_title = pacon_datas.objects.values()
    data['list'] = list(data_title)
    for i in range(len(data_title)):
        datas[i] = data['list'][i]
    for m in range(len(data_title)):
        res[m]['title'] = datas[m]['title_news']
        res[m]['time'] = datas[m]['times_news']
        res[m]['read'] = datas[m]['reads_news']
        res[m]['body'] = datas[m]['body_news']
        res[m]['image'] = datas[m]['images']
    reads = dict(res)
    return reads
