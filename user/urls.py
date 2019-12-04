# _*_ coding : UTF-8 _*_
# 开发人员："夏沫丶"
# 开发时间： 2019/11/30 18:21
# 文件名称： urls.py.py
# 开发工具： PyCharm
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="index")
]
