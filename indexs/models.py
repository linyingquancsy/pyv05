from django.db import models

# Create your models here.
class iot_data(models.Model):
    '''
    爬虫数据存储表：
    'tem': "#",
    'hum': "#",
    'somken': "#",
    'mea': "#",
    'door': "#",
    'winzhu': "#",
    'winci': "#",
    'people': "#",
    'cpu': "#"

    模型变更：
    python manage.py makemigrations
    python manage.py migrate --database=iot
    '''

    tem = models.TextField()
    hum = models.TextField()
    somken = models.TextField()
    mea = models.TextField()
    door = models.TextField()
    winzhu = models.TextField()
    winci = models.TextField()
    people = models.TextField()
    cpu = models.TextField()
