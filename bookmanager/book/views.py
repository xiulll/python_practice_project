from django.shortcuts import render

# Create your views here.
#视图就是一个Python函数，被定义在应用的views.py中.
# 视图的第一个参数是HttpRequest类型的对象reqeust，包含了所有请求信息.
# 视图必须返回HttpResponse对象，包含返回给请求者的响应信息.
# 需要导入HttpResponse模块 :from django.http import HttpResponse

from django.http import HttpRequest
from django.http import HttpResponse

def index(request):
    return HttpResponse("ok!")