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
