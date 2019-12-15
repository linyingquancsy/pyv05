'''
爬取‘四川工程职业技术学院 官网新闻’
'''

import requests
from scrapy import Selector
from urllib import parse
from collections import defaultdict

url = "https://www.scetc.edu.cn/2294/list.htm"
domin = 'https://www.scetc.edu.cn/'
datas = defaultdict(dict)

def resquest_data(url):
    html = requests.get(url)
    bian = html.apparent_encoding
    html.encoding = bian
    html = html.text
    return html

def get_next_url(html):
    '''
    获取下一页url
    :param html:
    :return:
    '''
    sel = Selector(text=html)
    next_urls = sel.xpath(''' //*[@id="wp_paging_w9"]/ul/li[2]/a[3]/@href ''').extract()
    if next_urls:
        next_url = parse.urljoin(domin, next_urls[0])
    return str(next_url)

def get_body_data(urls):
    '''
    传入新闻页面内容，获取单个页面的内容，文本内容
    :return: 文本内容
    '''
    html = resquest_data(urls)
    sel = Selector(text=html)
    bodys_list = sel.xpath('''  /html/body/div[4]/div/div[2]/div[1]/div/div[2]/div/div[2]/article/div//p//span /text() ''').extract()
    bodys_str = body_str.str_init(bodys_list)    # bodys_str中保存的是文本内容字符串
    # bodys_str = bodys_list    # bodys_str中保存的是文本内容字符串
    return bodys_str

class body_str():
    def str_init(list_data):
        str_data = ""
        # for i in list_data:
        for j in range(len(list_data)):
        # for j in range(5):
            str_data += list_data[j]
        return str_data

def reads_data(urls):
    '''
    获取单页访问量
    :return:
    '''
    html = resquest_data(urls)
    sel = Selector(text=html)
    read_list = sel.xpath(''' /html/body/div[4]/div/div[2]/div[1]/div/div[2]/div/p/span[2]/span/text() ''').extract()
    return int(read_list[0])

def images_data(urls):
    '''
    获取图片url，
    :return: 保存图片url的列表
    '''
    html = resquest_data(urls)
    sel = Selector(text=html)
    read_list = sel.xpath(''' /html/body/div[4]/div/div[2]/div[1]/div/div[2]/div/div[2]/article/div//p//img/@src ''').extract()
    x = 0
    images_data_url = []
    for reads in read_list:
        reads_lists = parse.urljoin(domin, reads)
        x = x+1
        images_data_url.append(reads_lists)
    return images_data_url

def all_data():
    '''
    获取body，reads，image数据，并存入datas中
    :return:
    '''
    i = 0
    for url_ts in datas.values():
        news_str = get_body_data(url_ts['urls'])
        datas[i]['bodys'] = news_str
        datas[i]['reads'] = reads_data(url_ts['urls'])
        datas[i]['images'] = images_data(url_ts['urls'])
        i = i+1

def scetc_news(html):
    '''
    获取列表栏单个页面url，标题，时间
    :param html:
    :return:
    '''
    i = 0
    sel = Selector(text=html)
    all_li = sel.xpath('''//div[@id="wp_news_w9"]/ul//li''')
    for tra in all_li:
        url_news = tra.xpath("//span[1]/a/@href").extract()
        title_news = tra.xpath("//span[1]/a/@title").extract()
        times_news = tra.xpath("//span[@class='column-news-date news-date-hide']/text()").extract()
    for i in range(len(url_news)):
        datas[i]['urls'] = parse.urljoin(domin, url_news[i])
        datas[i]['titles'] = title_news[i]
        datas[i]['times'] = times_news[i]

def all_mtml_main(urls_index):
    scetc_news(resquest_data(urls_index))
    all_data()
    return datas

if __name__ == '__main__':
    a = 20
    url_text = url
    print(url_text)
    while a:
        url_text = get_next_url(resquest_data(url_text))
        print(url_text)
        a = a - 1


