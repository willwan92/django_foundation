from django.http import HttpResponse
import json


# Create your views here.

def weather(request, city, date):
    print(city, date)
    return HttpResponse('weather')


# GET /get_query_params?a=1&b=2&b=3
def get_query_params(request):
    query_dict = request.GET
    # 获取单个值，返回字符串
    a = query_dict.get('a')
    # 获取某个参数的多个值，返回字符串列表
    b = query_dict.getlist('b')
    return HttpResponse('get_query_params: a=%s, b=[%s, %s]' % (a, b[0], b[1]))


# POST /get_form_data
def get_form_data(request):
    query_dict = request.POST
    # 获取单个值，返回字符串
    lang = query_dict.get('lang')
    # 获取某个参数的多个值，返回字符串列表
    framework = query_dict.getlist('framework')
    return HttpResponse('get_form_data: lang=%s, framework=[%s, %s]' % (lang, framework[0], framework[1]))


# POST /get_json
def get_json(request):
    # request.body 获取请求体中的非表单数据，得到bytes对象类型数据
    json_bytes = request.body
    json_str = json_bytes.decode()
    # json.loads把json字符串解析为字典或json列表
    params_dict = json.loads(json_str)
    # 获取某个参数的多个值，返回字符串列表
    name = params_dict.get('name')
    age = params_dict.get('age')
    return HttpResponse('get_json: name=%s, age=%d' % (name, age))
