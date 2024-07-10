from django.http import HttpResponse

# Create your views here.

def weather(request, city, date):
    print(city, date)
    return HttpResponse('weather')
