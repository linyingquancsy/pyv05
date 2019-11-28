from django.http import HttpResponse
# Create your views here.
def cs(request):
    text = "这是一个测试接口"
    return HttpResponse(text)