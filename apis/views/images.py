'''
图片上传
'''
import os
import hashlib
from django.http import HttpResponse, FileResponse, Http404, JsonResponse
from pyv05 import settings
import utils.response
from django.views import View   # 类视图继承的类

'''
django图文消息的应用（实现在小程序上进行文件的增删改查）
django的文件操作（os库）
继承了response.ResponseMixin的类
'''
class File_image(View, utils.response.ResponseMixin):
    def get(self, request):
        '''
        对文件进行查询
        :param request:
        :return:
        '''
        md5 = request.GET.get('md5')                        # 获取url上的参数md5  =>  ...?md5=name
        img_name = md5 + '.jpg'
        path = os.path.join(settings.IMAGES_DIR, img_name)  # 对参数进行处理，生成图片文件的路径
        print(path)
        if os.path.exists(path):                            # 判断文件是否存在
            data = open(path, 'rb').read()
            return FileResponse(open(path, 'rb'), content_type='image/jpg') # 存在则返回图片数据
        else:
            response = self.wrap_json_response(data='not file')
            return JsonResponse(data=response, safe=False)  # 不存在则返回json数据，数据的data为not file

    def post(self, request):
        '''
        对文件进行上传
        :param request:
        :return:
        '''
        files = request.FILES               # 接收客户端上传上来的数据（如微信小程序中的wx.uploadFile() Post方法的）
        print('$$$', files)
        response = []
        for key,value in files.items():
            content = value.read()          # 将图片数据的value部分取出
            md5 = hashlib.md5(content).hexdigest()  # 使用hex工具进行解码
            path = os.path.join(settings.IMAGES_DIR, 'resqut.jpg')  # 获取图片保存的路径
            with open(path, 'wb') as f:
                f.write(content)            # 往文件中写入数据（解码后图片的数据）
            print('md5:', md5)
            print('contant:', content)
            response.append({               # 往response列表中添加字典数据，为name（客户端上传时的文件名称test），和md5（图片本身的名字）
                'name': key,
                'md5': md5
            })
        print('list:', response)
        message = 'post'
        response_json = self.wrap_json_response(data=response, code='111', message=message)
        return JsonResponse(data=response_json, safe=False)  # 返回json格式的数据，为图片名字，和md5

    def delete(self, request):
        '''
        对本地文件进行删除
        :param request:
        :return:
        '''
        md5 = request.GET.get('md5')
        img_name = md5 + '.jpg'
        path = os.path.join(settings.IMAGES_DIR, img_name)  # 获取文件完整路径
        print(path)
        if os.path.exists(path):        # 判断文件是否存在
            os.remove(path)             # 利用os库对文件进行删除
            message = '删除成功'
        else:
            message = 'file(%s) not found.' % img_name  # 不存在则返回不存在的字符串
        response = self.wrap_json_response(code='code', message=message)
        return JsonResponse(data=response, safe=False)   # 利用json格式数据返回

'''
综合实践---生活服务，图片备份功能优化
加入，自动加载，删除预览，保存本地，取消上传等功能
'''
class ImageListView(View, utils.response.ResponseMixin):
    def get(self,request):
        image_file = os.listdir(settings.IMAGES_DIR)
        response_data = []
        for i in image_file:
            response_data.append(
                {
                    "name":i,
                    "md5":i[:-4]
                }
            )
        print('list: ',response_data)
        response_data = self.json_response(data=response_data)
        return JsonResponse(data=response_data)
