'''
优化url地址，新增版本号
'''

from django.urls import path, include


urlpatterns = [
    path('service/', include('apis.urls')),    # 转发信息到 apis.urls 中
]

