'''
这是一个给app加状态码的一个类函数
状态码有什么用，现在还不知道，对于实验级别的应用，可以不加吧！
'''

# 状态码
class ReturnCode:
    SUCCESS = 0
    FAILED = -100
    UNAUTHORIZED = -500
    BROKEN_AUTHORIZED_DATA = -501
    WRONG_PARMAS = -101
    RESOURCES_NOT_EXITSTS = 404
    @classmethod
    def message(cls,code):
        if code == cls.SUCCESS:
            return 'success'
        elif code == cls.FAILED:
            return 'failed'
        elif code == cls.UNAUTHORIZED:
            return 'unautgorized'
        elif code == cls.WRONG_PARMAS:
            return 'wrong parmas'
        elif code == cls.RESOURCES_NOT_EXITSTS:
            return 'RESOURCES_NOT_EXITSTS***'
        else:
            return ''


# def wrap_json_response(data=None, code=None, message=None):
#     response = {}
#     if not code:
#         code = ReturnCode.SUCCESS
#     if not message:
#         pass
#     if data:
#         response['data'] = data
#     response['result_code'] = code
#     response['message'] = message
#     return response

'''
定义一个Mixin模式的类
在images中有使用此类的示例代码
'''
class ResponseMixin(object):
    @classmethod
    def wrap_json_response(cls, data=None, code=None, message=None):
        response = {}
        if not code:
            code = ReturnCode.SUCCESS
        if not message:
            pass
        if data:
            response['data'] = data
        response['result_code'] = code
        response['message'] = message
        return response





