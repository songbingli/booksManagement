# 自定义中间件类
from django.shortcuts import redirect

import re

from django.urls import reverse


class BookMiddleware(object):
    """
    图书管理系统中间件
    """
    def __init__(self, get_response):
        """
        中间件初始化
        :param get_response:
        """
        self.get_response = get_response

    def __call__(self, request):
        """
        中间件功能运行
        :param request:
        :return:
        """
        # 定义不用登录也可访问的路由url
        urllist = ['/login', '/do_login', '/logout', '/verify', '/register', '/do_register']
        # 获取当前请求路径
        path = request.path
        # print("Hello World!"+path)
        # 判断当前请求是否是访问网站前台,并且path不在urllist中
        if re.match("/", path) and (path not in urllist) and (not re.match("/admin", path)):
            # 判断当前用户是否没有登录
            if "user_name" not in request.session:
                # 执行登录界面跳转
                return redirect(reverse('bookMS:bookMS_login'))
        response = self.get_response(request)

        return response
