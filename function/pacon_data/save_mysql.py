# -*- coding: UTF-8 -*-
import os
import django
import random
from pacon_data.get_scetc import *

# 创建Django环境
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'pyv03.settings')
django.setup()
from app_get_data.models import pacon_datas

def ranstr(lenght):
    '''
    用于随机生成一个lenght的字符串
    :param lenght:  字符串长度
    :return:  随机生成的字符串
    '''
    CHS = 'QWERTYUIOPASDFGHJKLZXCVBNMqwertyuiopasdfghjklzxcvbnm1234567890'
    salt = ''
    for i in range(lenght):
        salt += random.choice(CHS)
    return salt


class body_str():
    def str_init(list_data):
        '''
        将列表拼接成字符串
        :return:
        '''
        str_data = ""
        # for i in list_data:
        # for j in range(len(list_data)):
        for j in list_data:
            str_data = str_data + j + ' '
        return str_data

def add_batch1(datas):
    '''
    批量存储数据
    :return:
    '''
    new_user_list = []
    # 用于向列表中添加数据
    for i in datas.values():
        openid = ranstr(32)
        urls_new = i['urls']
        titles_new = i['titles']
        times_new = i['times']
        bodys_new = i['bodys']
        reads_new = i['reads']
        images_new = body_str.str_init(i['images'])
        user = pacon_datas(openid=openid, urls_news=urls_new, title_news=titles_new, times_news=times_new, reads_news=reads_new, body_news=bodys_new, images=images_new)
        new_user_list.append(user)
    # 批量添加数据，（将列表中的数据批量添加到数据库中）
    pacon_datas.objects.bulk_create(new_user_list)
    print("批量存储数据成功！")

def delete_all():
    '''
    全部删除
    :return:
    '''
    pacon_datas.objects.all().delete()
    print("数据库全部数据删除完毕！")
url = "https://www.scetc.edu.cn/2294/list.htm"

if __name__ == '__main__':
    # 删除数据库所有数据
    # delete_all()

    '''
    保存官网新闻前10页的数据
    '''
    a = 9
    url_text = url
    print(url_text)
    datas = dict(all_mtml_main(url_text))
    add_batch1(datas)
    while a:
        url_text = get_next_url(resquest_data(url_text))
        datas = dict(all_mtml_main(url_text))
        add_batch1(datas)
        print(url_text)
        a = a - 1
