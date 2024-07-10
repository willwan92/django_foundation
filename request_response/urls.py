from django.urls import re_path
from . import views

urlpatterns = [
    # 使用正则组提取url路径参数(位置参数)
    # re_path(r"^weather/([a-z]+)/(\d{8})/$", views.weather),
    # 使用正则命名组提取url路径参数(关键字参数)，使用命名组时视图函数的形参必须和正则组名称一致
    re_path(r'^weather/(?P<city>\w+)/(?P<date>\d{8})/$', views.weather),
]
