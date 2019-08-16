from django.shortcuts import render


def index(request):
    """
    图书管理系统首页
    :param request:
    :return:
    """
    return render(request, "bookMS/index.html")
