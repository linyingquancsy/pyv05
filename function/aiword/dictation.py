
from aip import AipOcr
from pyv05 import settings

APP_ID = '17881269'
API_KEY = 'xU0METzpo28Mx5PrwKHGaIG1'
SECRET_KEY = 'aT96Gz1kOipliiwyl1Cdgt9WBA2Rm3A7'
client = AipOcr(APP_ID, API_KEY, SECRET_KEY)

# 读取图片
filePath = settings.IMAGES_DIR + "\\resqut.jpg"
print('@@@',filePath)
def get_file_content(filePath):
    with open(filePath, 'rb') as fp:
        return fp.read()

def text_baidu(filePath):
    '''
    调用手写文字识别
    :param filePath: 图片位置
    :return: 识别结果
    '''
    image = get_file_content(filePath)


    try:
        texttap = client.handwriting(image)
        data = []
        for i in texttap['words_result']:
            data.append(i['words'])
        return data
    except:
        texttap = client.basicGeneral(image)
        data = []
        for i in texttap['words_result']:
            data.append(i['words'])
        return data

