from django.http import HttpResponse

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
    return HttpResponse('get_query_params: lang=%s, framework=[%s, %s]' % (lang, framework[0], framework[1]))