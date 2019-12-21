'''
多线程爬取‘四川工程职业技术学院 官网新闻’
'''

import requests
from scrapy import Selector
from urllib import parse
from collections import defaultdict
import time
from threading import Thread
from function.pacon_data.get_scetc import *

url_index = "https://www.scetc.edu.cn/2294/list.htm"
domin = 'https://www.scetc.edu.cn/'
# datas = defaultdict(dict)

class ParseTopicListThread(Thread):
    def run(self):
        all_mtml_main1()

class ParseTopicDataThread(Thread):
    def run(self):
        all_mtml_main2()

if __name__ == '__main__':
    topic_list_thread = ParseTopicListThread()
    topic_data_thread = ParseTopicDataThread()
    topic_list_thread.start()
    topic_data_thread.start()
    topic_list_thread.join()
    topic_data_thread.join()

    print(datas)
