# _*_ coding : UTF-8 _*_
# 开发人员："夏沫丶"
# 开发时间： 2019/12/1 14:05
# 文件名称： views.py
# 开发工具： PyCharm
from django.http import HttpResponse

def hell(request):
    return HttpResponse("hello world")