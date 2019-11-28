'''
对app应用进行路由
'''

from django.urls import path
from .views import images, cs, aiword, aivoice

urlpatterns = [
    # 测试接口
    path('cs', cs.cs),      # 优化图片备份的路由地址

    # 路由时使用类视图的时候，需要调用 as_view() 函数
    path('imageFile', images.File_image.as_view()),          # 这是微信小程序上传和删除图片的url路由地址（http://127.0.0.1:8000/api/v1.0/service/imageFile?md5=001）

    path('image/list', images.ImageListView.as_view()),      # 优化图片备份的路由地址

    path('aiword', aiword.aiword.as_view()),                 # 返回识别结果
    path('aivoice', aivoice.aivoice.as_view()),               # 返回读音
    path('voicePlay', aivoice.voicePlay.as_view()),             # 返回读音
    path('voice', aivoice.filevoice.as_view()),               # 返回读音
]

