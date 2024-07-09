# from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.

def index(request):
    """
    视图函数，django函数视图最少要有一个参数
    :params request 接收请求对象 类型HttpRequest
    :return 响应对象 HttpResponse
    """

    return HttpResponse('hello world')
