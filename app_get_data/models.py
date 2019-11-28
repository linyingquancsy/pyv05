from django.db import models

class pacon_datas(models.Model):
    '''
    爬虫数据存储表：
    openid
    url
    标题
    时间
    阅读量
    文本内容
    图片

    模型变更：
    python manage.py makemigrations
    python manage.py migrate
    '''
    openid = models.CharField(max_length=32, unique=True)
    urls_news = models.URLField()
    title_news = models.TextField()
    times_news = models.TextField()
    reads_news = models.CharField(max_length=32)
    body_news = models.TextField()
    images = models.TextField()

    def __str__(self):
        return '%s(%s)' % (self.title_news, self.openid)